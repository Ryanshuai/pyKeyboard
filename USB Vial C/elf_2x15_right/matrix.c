/*
 * 右手 2×15 矩阵 + 6 线性键 自定义扫描
 * 
 * ==================== GPIO 布线说明 ====================
 * 
 * 根据实际焊接（从正面看右手键盘，左到右）：
 *   - 左边3列（内侧，靠近拇指）= GP1 红色边框
 *   - 右边3列（外侧，远离拇指）= GP2 绿色边框
 * 
 * ==================== 右手物理布局（从正面看）====================
 * 
 *     物理列:   0      1      2    |   3      4      5
 *              ←── 内侧(GP1) ──→   | ←── 外侧(GP2) ──→
 *              (红色边框)           | (绿色边框)
 * 
 * 物理行0:  GP3    GP8    GP13  |  GP3   (空)   (空)
 * 物理行1:  GP4    GP9    GP14  |  GP4    GP9    GP14
 * 物理行2:  GP5    GP10   GP15  |  GP5    GP10   GP15
 * 物理行3:  GP6    GP11   GP16  |  GP6    GP11   GP16
 * 物理行4:  GP7    GP12   GP17  |  GP7    GP12   GP17
 * 
 * 列线从内到外: GP3/4/5/6/7, GP8/9/10/11/12, GP13/14/15/16/17
 * 
 * 拇指区（从左到右，平铺）：GP18, GP19, GP20, GP21, GP22, GP26
 * 
 * ==================== 矩阵映射 ====================
 * 
 * vial.json keymap 每行的布局:
 *   ["0,0", "0,1", "0,2", "1,0", "1,1", "1,2"]
 *     ↑ row0 内侧(GP1) ↑   ↑ row1 外侧(GP2) ↑
 * 
 * 所以 row_pins[0] = GP1（内侧），row_pins[1] = GP2（外侧）
 */

#include "quantum.h"

// 矩阵行引脚（2根）
// 右手：row0 = GP1（内侧，红色边框），row1 = GP2（外侧，绿色边框）
static const pin_t row_pins[] = { GP1, GP2 };
#define MATRIX_ROW_COUNT 2

// 矩阵列引脚（15根）
// 按物理行排列，每行从内到外: GP3/4/5/6/7, GP8/9/10/11/12, GP13/14/15/16/17
static const pin_t col_pins[] = { 
    GP3,  GP8,  GP13,   // 物理行0的列线（内侧到外侧）
    GP4,  GP9,  GP14,   // 物理行1的列线
    GP5,  GP10, GP15,   // 物理行2的列线
    GP6,  GP11, GP16,   // 物理行3的列线
    GP7,  GP12, GP17    // 物理行4的列线
};
#define MATRIX_COL_COUNT 15

// 线性键引脚（6根，作为逻辑第3行）
// 右手拇指区从左到右：GP18, GP19, GP20, GP21, GP22, GP26
static const pin_t direct_pins[] = { GP18, GP19, GP20, GP21, GP22, GP26 };
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
