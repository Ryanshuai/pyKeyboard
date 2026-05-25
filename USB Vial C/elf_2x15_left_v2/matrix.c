/*
 * 左手 2×15 矩阵 + 6 直连键 自定义扫描 (v2)
 *
 * ==================== 变更说明 ====================
 * - GPIO 全部前移一位: GP0-GP22 连续, 不再使用 GP26
 * - 列线交叉映射: 内外同向排列, 同GP两键间隔≥2, 无二极管不鬼键
 * - 列线顺序: pos1(靠Pico)=GP2-6, pos2(中间)=GP7-11, pos3(远)=GP12-16
 * - 左手硬件是右手镜像, row_pins/col_pins 做镜像补偿
 *   (keymap 和 keyboard.json 沿用右手布局, 不动)
 *
 * ==================== GPIO 布线说明 ====================
 *
 * 物理行线 (2根, 漆包线蛇形):
 *   GP0 = 内侧行线 (物理) → 软件映射为 row1
 *   GP1 = 外侧行线 (物理) → 软件映射为 row0
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
 *
 * ==================== 交叉映射说明 ====================
 *
 * 背面视角 (内侧在左, 外侧在右):
 *   内侧 pos1  pos2  pos3  |  外侧 pos4  pos5  pos6
 *   同GP两键: (pos1,pos4) (pos2,pos5) (pos3,pos6) 间隔≥2
 */

#include "quantum.h"

// 行线: 左手物理是右手镜像, 软件做镜像补偿
//   GP0 物理接到内侧(对应右手row0=内侧), 但左手内侧是 keymap [1,*]
//   所以这里把 row0/row1 互换, 让 GP1(外侧)=row0, GP0(内侧)=row1
static const pin_t row_pins[] = { GP1, GP0 };
#define MATRIX_ROW_COUNT 2

// 列线: 15根, 按物理行排列
// 每行: pos3(远=外侧最外), pos2(中间), pos1(靠Pico=内侧最里) ← 镜像后反序
// 这样 col_pins[0..2] 对应 visual x=0,1,2 (左手外侧, keymap [0,*])
static const pin_t col_pins[] = {
    GP12, GP7,  GP2,    // 行0 (镜像反序)
    GP13, GP8,  GP3,    // 行1
    GP14, GP9,  GP4,    // 行2
    GP15, GP10, GP5,    // 行3
    GP16, GP11, GP6     // 行4
};
#define MATRIX_COL_COUNT 15

// 拇指区直连: 左手物理是右手镜像, 这里反序
// 让两手在对称物理位置出对称 modifier (e.g. 两手 inner-top 都是 C+F8)
static const pin_t direct_pins[] = { GP22, GP21, GP20, GP19, GP18, GP17 };
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
