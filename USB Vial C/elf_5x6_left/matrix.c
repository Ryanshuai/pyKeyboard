/*
 * 自定义矩阵扫描
 * 
 * 矩阵键 (5x6):
 *   行: GP1, GP2, GP3, GP4, GP5
 *   列: GP6, GP7, GP8, GP9, GP10, GP11
 * 
 * 线性键 (6个独立GPIO，作为第6行):
 *   GP12, GP13, GP14, GP15, GP16, GP17
 */

#include "quantum.h"

// 矩阵行引脚 (5行)
static const pin_t row_pins[] = { GP1, GP2, GP3, GP4, GP5 };
#define MATRIX_ROW_COUNT 5

// 矩阵列引脚 (6列)
static const pin_t col_pins[] = { GP6, GP7, GP8, GP9, GP10, GP11 };
#define MATRIX_COL_COUNT 6

// 线性键引脚 (6个独立按键，作为第6行)
static const pin_t direct_pins[] = { GP12, GP13, GP14, GP15, GP16, GP17 };
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
    
    // 扫描矩阵键 (前5行, COL2ROW)
    for (int row = 0; row < MATRIX_ROW_COUNT; row++) {
        // 拉低当前行
        gpio_write_pin_low(row_pins[row]);
        matrix_io_delay();
        
        matrix_row_t row_data = 0;
        for (int col = 0; col < MATRIX_COL_COUNT; col++) {
            // 列为低电平表示按下
            if (!gpio_read_pin(col_pins[col])) {
                row_data |= (1 << col);
            }
        }
        
        // 恢复当前行为高电平
        gpio_write_pin_high(row_pins[row]);
        
        if (current_matrix[row] != row_data) {
            current_matrix[row] = row_data;
            changed = true;
        }
    }
    
    // 扫描线性键 (第6行，索引5)
    // 按下时为低电平（value_when_pressed=False, pull=True）
    matrix_row_t direct_row = 0;
    for (int i = 0; i < DIRECT_PIN_COUNT; i++) {
        if (!gpio_read_pin(direct_pins[i])) {
            direct_row |= (1 << i);
        }
    }
    
    if (current_matrix[5] != direct_row) {
        current_matrix[5] = direct_row;
        changed = true;
    }
    
    return changed;
}
