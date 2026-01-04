/*
 * 左手 2×15 矩阵 + 6 线性键 自定义扫描
 * 
 * ==================== 根据 SVG 图的 GPIO 布线 ====================
 * 
 * 左手物理布局（从左到右看，正面）：
 *     物理列:   0      1      2    |   3      4      5
 *              ←── 左半边(GP1) ──→ | ←── 右半边(GP2) ──→
 * 
 * 物理行1:  (空)   (空)   GP3   |  GP13   GP8    GP3
 * 物理行2:  GP14   GP9    GP4   |  GP14   GP9    GP4
 * 物理行3:  GP15   GP10   GP5   |  GP15   GP10   GP5
 * 物理行4:  GP16   GP11   GP6   |  GP16   GP11   GP6
 * 物理行5:  GP17   GP12   GP7   |  GP17   GP12   GP7
 * 
 * 拇指区（从左到右）：GP26, GP22, GP21, GP20, GP19, GP18
 */

#include "quantum.h"

// 矩阵行引脚（2根）
static const pin_t row_pins[] = { GP1, GP2 };
#define MATRIX_ROW_COUNT 2

// 矩阵列引脚（15根）
// 左手列线顺序（从左到右）：每行是 GP13/14/15/16/17, GP8/9/10/11/12, GP3/4/5/6/7
// 但由于同一物理行的左右两边共用列线，按物理行排列：
static const pin_t col_pins[] = { 
    GP13, GP8,  GP3,    // 物理行0的列线
    GP14, GP9,  GP4,    // 物理行1的列线
    GP15, GP10, GP5,    // 物理行2的列线
    GP16, GP11, GP6,    // 物理行3的列线
    GP17, GP12, GP7     // 物理行4的列线
};
#define MATRIX_COL_COUNT 15

// 线性键引脚（6根，作为逻辑第3行）
// 左手拇指区从左到右：GP26, GP22, GP21, GP20, GP19, GP18
// 注意：GP23 在 Pico 上被电源芯片占用，改用 GP26
static const pin_t direct_pins[] = { GP26, GP22, GP21, GP20, GP19, GP18 };
#define DIRECT_PIN_COUNT 6

void matrix_init_custom(void) {
    // 初始化矩阵行引脚为输出，默认高电平
    for (int i = 0; i < MATRIX_ROW_COUNT; i++) {
        gpio_set_pin_output(row_pins[i]);
        gpio_write_pin_high(row_pins[i]);
    }
    
    // 初始化矩阵列引脚为输入，上拉
    for (int i = 0; i < MATRIX_COL_COUNT; i++) {
        gpio_set_pin_input_high(col_pins[i]);
    }
    
    // 初始化线性键引脚为输入，上拉
    for (int i = 0; i < DIRECT_PIN_COUNT; i++) {
        gpio_set_pin_input_high(direct_pins[i]);
    }
}

bool matrix_scan_custom(matrix_row_t current_matrix[]) {
    bool changed = false;
    
    // 扫描矩阵键（前2行）
    for (int row = 0; row < MATRIX_ROW_COUNT; row++) {
        // 拉低当前行
        gpio_write_pin_low(row_pins[row]);
        matrix_io_delay();
        
        matrix_row_t row_data = 0;
        for (int col = 0; col < MATRIX_COL_COUNT; col++) {
            if (!gpio_read_pin(col_pins[col])) {
                row_data |= ((matrix_row_t)1 << col);
            }
        }
        
        // 恢复当前行为高电平
        gpio_write_pin_high(row_pins[row]);
        
        if (current_matrix[row] != row_data) {
            current_matrix[row] = row_data;
            changed = true;
        }
    }
    
    // 扫描线性键（第3行，索引2）
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
