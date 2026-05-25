// RP2040 GPIO capacitance probe
// 通过测量"放电后内部上拉充到 high 所需的循环次数"估算每个 GPIO 的对地电容
// 数值越大 = 焊的线越长/触点越多 = 电容越大

#include <stdio.h>
#include "pico/stdlib.h"
#include "pico/bootrom.h"
#include "hardware/gpio.h"
#include "hardware/pio.h"
#include "hardware/timer.h"
#include "toggle.pio.h"

// Pico 板上可用的 GPIO (排除 GP23/24/25 板载用、GP29 ADC VSYS)
static const uint PINS[] = {
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
    12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
    26, 27, 28
};
#define N_PINS (sizeof(PINS) / sizeof(PINS[0]))

#define MAX_COUNT 5000
#define SAMPLES   15

static uint32_t measure_pin(uint gpio) {
    // 1. 初始化并输出 low 放电
    gpio_init(gpio);
    gpio_set_dir(gpio, GPIO_OUT);
    gpio_put(gpio, 0);
    sleep_us(1000);  // 充分放电

    // 2. 切输入 + 上拉，开始数循环
    gpio_set_dir(gpio, GPIO_IN);
    gpio_pull_up(gpio);

    uint32_t count = 0;
    while (!gpio_get(gpio) && count < MAX_COUNT) {
        count++;
    }

    // 3. 测完钳到 low，防止悬空漂移干扰相邻脚
    gpio_disable_pulls(gpio);
    gpio_set_dir(gpio, GPIO_OUT);
    gpio_put(gpio, 0);
    return count;
}

static uint32_t median(uint32_t *a, int n) {
    // 简单插入排序
    for (int i = 1; i < n; i++) {
        uint32_t k = a[i];
        int j = i - 1;
        while (j >= 0 && a[j] > k) { a[j+1] = a[j]; j--; }
        a[j+1] = k;
    }
    return a[n/2];
}

static void scan_once(void) {
    printf("pin,count\n");
    for (int i = 0; i < N_PINS; i++) {
        uint32_t s[SAMPLES];
        for (int k = 0; k < SAMPLES; k++) s[k] = measure_pin(PINS[i]);
        printf("GP%u,%lu\n", PINS[i], (unsigned long)median(s, SAMPLES));
    }
    printf("END\n");
}

// 把所有"其它"引脚设为输入高阻 (中性, 不影响测量)
static void isolate_others(uint keep_a, uint keep_b) {
    for (int i = 0; i < N_PINS; i++) {
        uint p = PINS[i];
        if (p != keep_a && p != keep_b) {
            gpio_set_dir(p, GPIO_IN);
            gpio_disable_pulls(p);
        }
    }
}

// 差分法测 A 对 B 的互电容耦合:
//   count_low  = B 在 A=0 时的上拉充电循环次数
//   count_high = B 在 A=1 时的上拉充电循环次数
// A=low 时, 互电容会"吸"B 的电荷 → B 充得慢 → count_low 更大
// 返回 (count_low - count_high) 的平均值, 数值越大代表 A-B 耦合越强
#define MC_MAX 3000
#define MC_SAMPLES 8

static int32_t measure_mutual(uint a, uint b) {
    isolate_others(a, b);

    int32_t sum = 0;
    for (int k = 0; k < MC_SAMPLES; k++) {
        // --- A = low ---
        gpio_disable_pulls(a); gpio_set_dir(a, GPIO_OUT); gpio_put(a, 0);
        gpio_disable_pulls(b); gpio_set_dir(b, GPIO_OUT); gpio_put(b, 0);
        sleep_us(300);
        gpio_set_dir(b, GPIO_IN); gpio_pull_up(b);
        uint32_t c0 = 0;
        while (!gpio_get(b) && c0 < MC_MAX) c0++;

        // --- A = high ---
        gpio_disable_pulls(b); gpio_set_dir(b, GPIO_OUT); gpio_put(b, 0);
        gpio_put(a, 1);
        sleep_us(300);
        gpio_set_dir(b, GPIO_IN); gpio_pull_up(b);
        uint32_t c1 = 0;
        while (!gpio_get(b) && c1 < MC_MAX) c1++;

        sum += (int32_t)c0 - (int32_t)c1;
    }

    // 复位
    gpio_disable_pulls(a); gpio_set_dir(a, GPIO_OUT); gpio_put(a, 0);
    gpio_disable_pulls(b); gpio_set_dir(b, GPIO_OUT); gpio_put(b, 0);

    return sum / MC_SAMPLES;
}

// ==================== PIO 方波 + 电荷积分法 ====================
//
// 原理:
//   1. B 放电到 0V, 然后切高阻无上拉
//   2. A 由 PIO 驱动, 以 ~62.5 MHz 方波翻转
//   3. 每个上升沿通过互电容 Cab 向 B 注入电荷 ΔQ = Cab × VDD
//   4. B 电位累积上升, 计时到 B 读数变 high
//   5. 时长 dt(µs) 与 Cab 成反比: Cab 越大, dt 越短
//
// 优势: 62.5 MHz 翻转远快过 C 循环, 漏电对结果影响小千倍
//
static PIO  g_pio    = pio0;
static uint g_sm     = 0;
static uint g_offset = 0;

static void pio_init_once(void) {
    g_offset = pio_add_program(g_pio, &toggle_fast_program);
}

#define PIO_TIMEOUT_US 2000

static uint32_t measure_mutual_pio(uint a, uint b) {
    // 其它 pin 高阻无拉
    isolate_others(a, b);

    // 把 A 和 B 都放电
    gpio_init(a); gpio_disable_pulls(a);
    gpio_set_dir(a, GPIO_OUT); gpio_put(a, 0);
    gpio_init(b); gpio_disable_pulls(b);
    gpio_set_dir(b, GPIO_OUT); gpio_put(b, 0);
    sleep_us(800);

    // B 浮空输入
    gpio_set_dir(b, GPIO_IN);

    // 把 A 交给 PIO
    pio_gpio_init(g_pio, a);
    pio_sm_set_consecutive_pindirs(g_pio, g_sm, a, 1, true);

    pio_sm_config c = toggle_fast_program_get_default_config(g_offset);
    sm_config_set_set_pins(&c, a, 1);
    pio_sm_init(g_pio, g_sm, g_offset, &c);

    // 开启 PIO, 开始翻转
    pio_sm_set_enabled(g_pio, g_sm, true);

    uint32_t t0 = timer_hw->timerawl;
    uint32_t dt;
    while (1) {
        dt = timer_hw->timerawl - t0;
        if (gpio_get(b)) break;
        if (dt > PIO_TIMEOUT_US) { dt = PIO_TIMEOUT_US; break; }
    }

    // 关 PIO, 把 A 切回普通 GPIO 放电
    pio_sm_set_enabled(g_pio, g_sm, false);
    gpio_init(a); gpio_disable_pulls(a);
    gpio_set_dir(a, GPIO_OUT); gpio_put(a, 0);

    return dt;  // µs, 越小 = 耦合越强
}

static void scan_mutual_pio(void) {
    printf("mutual_cap_matrix_pio\n# unit: us to B reaching high; smaller = stronger coupling\n");
    printf("a\\b");
    for (int j = 0; j < N_PINS; j++) printf(",GP%u", PINS[j]);
    printf("\n");
    for (int i = 0; i < N_PINS; i++) {
        printf("GP%u", PINS[i]);
        for (int j = 0; j < N_PINS; j++) {
            if (i == j) { printf(",0"); continue; }
            uint32_t v = measure_mutual_pio(PINS[i], PINS[j]);
            printf(",%lu", (unsigned long)v);
        }
        printf("\n");
    }
    printf("END\n");
}

// 扫描全 NxN 矩阵并以 CSV 输出 (对角线填 0) —— 老的差分计数法
static void scan_mutual(void) {
    printf("mutual_cap_matrix\n");
    // header
    printf("a\\b");
    for (int j = 0; j < N_PINS; j++) printf(",GP%u", PINS[j]);
    printf("\n");
    for (int i = 0; i < N_PINS; i++) {
        printf("GP%u", PINS[i]);
        for (int j = 0; j < N_PINS; j++) {
            if (i == j) { printf(",0"); continue; }
            int32_t m = measure_mutual(PINS[i], PINS[j]);
            printf(",%ld", (long)m);
        }
        printf("\n");
    }
    printf("END\n");
}

int main(void) {
    stdio_init_all();
    pio_init_once();

    // 等 USB CDC 上位机连上（最多 10 秒，超时也继续）
    for (int i = 0; i < 100 && !stdio_usb_connected(); i++) sleep_ms(100);

    printf("\n# RP2040 GPIO capacitance probe ready\n");
    printf("# commands: M=self-cap, C=mutual-cap(diff), P=mutual-cap(PIO), B=bootloader\n");

    // 上电先测一次自电容
    scan_once();

    while (true) {
        int c = getchar_timeout_us(1000000);
        if (c == PICO_ERROR_TIMEOUT) continue;
        if (c == 'M' || c == 'm') {
            scan_once();
        } else if (c == 'C' || c == 'c') {
            scan_mutual();
        } else if (c == 'P' || c == 'p') {
            scan_mutual_pio();
        } else if (c == 'B' || c == 'b') {
            printf("entering bootloader...\n");
            sleep_ms(50);
            reset_usb_boot(0, 0);
        } else if (c == '?' || c == 'h' || c == 'H') {
            printf("# M=self-cap, C=mutual-cap, B=bootloader\n");
        }
    }
}
