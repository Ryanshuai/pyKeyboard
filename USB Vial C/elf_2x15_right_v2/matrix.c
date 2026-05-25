/*
 * 右手 2×15 矩阵 + 6 直连键 自定义扫描 (v2)
 *
 * ==================== 变更说明 ====================
 * - GPIO 全部前移一位: GP0-GP22 连续, 不再使用 GP26
 * - 列线交叉映射: 内外同向排列, 同GP两键间隔≥2, 无二极管不鬼键
 * - 列线顺序: pos1(靠Pico)=GP2-6, pos2(中间)=GP7-11, pos3(远)=GP12-16
 * - 左右手 matrix.c 完全相同 (镜像由物理焊接实现, 固件逻辑一致)
 *
 * ==================== GPIO 布线说明 ====================
 *
 * 行线 (2根, 漆包线蛇形):
 *   GP0 = 内侧行线 (row0)
 *   GP1 = 外侧行线 (row1)
 *
 * 列线 (15根, 彩色线到Pico):
 *   col_pins[] 按物理行排列, 每行3根 (pos1, pos2, pos3):
 *     行0: GP2,  GP7,  GP12   (红, 绿, 蓝 = RGB)
 *     行1: GP3,  GP8,  GP13   (紫, 紫, 紫)
 *     行2: GP4,  GP9,  GP14   (黄, 黄, 黄)
 *     行3: GP5,  GP10, GP15   (橙, 橙, 橙)
 *     行4: GP6,  GP11, GP16   (褐, 褐, 褐)
 *
 * 拇指区 (6根直连, 蛇形排列):
 *   GP17(红), GP18(绿), GP19(蓝), GP20(黄), GP21(橙), GP22(褐)
 */

#include "quantum.h"

// 行线: GP0(内侧), GP1(外侧)
static const pin_t row_pins[] = { GP0, GP1 };
#define MATRIX_ROW_COUNT 2

// 列线: 15根, 按物理行排列
// 每行: pos1(靠Pico), pos2(中间), pos3(远)
static const pin_t col_pins[] = {
    GP2,  GP7,  GP12,   // 行0 (RGB)
    GP3,  GP8,  GP13,   // 行1
    GP4,  GP9,  GP14,   // 行2
    GP5,  GP10, GP15,   // 行3
    GP6,  GP11, GP16    // 行4
};
#define MATRIX_COL_COUNT 15

// 拇指区直连 (6根, 蛇形: GP17→18→19→20→21→22)
static const pin_t direct_pins[] = { GP17, GP18, GP19, GP20, GP21, GP22 };
#define DIRECT_PIN_COUNT 6

void matrix_init_custom(void) {
    // 行线: 输出, 默认高
    for (int i = 0; i < MATRIX_ROW_COUNT; i++) {
        gpio_set_pin_output(row_pins[i]);
        gpio_write_pin_high(row_pins[i]);
    }

    // 列线: 输入上拉
    for (int i = 0; i < MATRIX_COL_COUNT; i++) {
        gpio_set_pin_input_high(col_pins[i]);
    }

    // 拇指直连: 输入上拉
    for (int i = 0; i < DIRECT_PIN_COUNT; i++) {
        gpio_set_pin_input_high(direct_pins[i]);
    }
}

bool matrix_scan_custom(matrix_row_t current_matrix[]) {
    bool changed = false;

    // 扫描矩阵键 (前2行)
    for (int row = 0; row < MATRIX_ROW_COUNT; row++) {
        gpio_write_pin_low(row_pins[row]);
        matrix_io_delay();

        matrix_row_t row_data = 0;
        for (int col = 0; col < MATRIX_COL_COUNT; col++) {
            if (!gpio_read_pin(col_pins[col])) {
                row_data |= ((matrix_row_t)1 << col);
            }
        }

        gpio_write_pin_high(row_pins[row]);

        if (current_matrix[row] != row_data) {
            current_matrix[row] = row_data;
            changed = true;
        }
    }

    // 扫描拇指直连键 (第3行, 索引2)
    matrix_row_t direct_row = 0;
    for (int i = 0; i < DIRECT_PIN_COUNT; i++) {
        if (!gpio_read_pin(direct_pins[i])) {
            direct_row |= ((matrix_row_t)1 << i);
        }
    }

    if (current_matrix[2] != direct_row) {
        current_matrix[2] = direct_row;
        changed = true;
    }

    return changed;
}
