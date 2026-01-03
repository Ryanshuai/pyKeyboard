/*
 * 2×15 矩阵 + 6 线性键 自定义扫描
 * 
 * ==================== GPIO 分配 ====================
 * 矩阵行（2根）：GP0, GP1
 * 矩阵列（15根）：GP2, GP3, GP4, GP5, GP6, GP7, GP8, GP9, GP10, GP11, GP12, GP13, GP14, GP15, GP16
 * 线性键（6根）：GP17, GP18, GP19, GP20, GP21, GP22
 * 
 * ==================== 布线方式 ====================
 * 
 * 物理布局（5行×6列）拆分成 2×15 逻辑矩阵：
 * 
 *     物理列: 0   1   2   3   4   5
 *            ←左半边→  ←右半边→
 * 物理行0:  [K0] [K1] [K2] [K3] [K4] [K5]
 * 物理行1:  [K6] [K7] [K8] [K9] [K10][K11]
 * 物理行2:  [K12][K13][K14][K15][K16][K17]
 * 物理行3:  [K18][K19][K20][K21][K22][K23]
 * 物理行4:  [K24][K25][K26][K27][K28][K29]
 * 
 * 逻辑矩阵：
 *   Row0（GP0）= 所有左半边（物理列 0-2）
 *   Row1（GP1）= 所有右半边（物理列 3-5）
 * 
 * 列线连接（每根只连 2 个键，物理上相邻）：
 *   Col0 (GP2):  K0 ←→ K3   (物理行0)
 *   Col1 (GP3):  K1 ←→ K4   (物理行0)
 *   Col2 (GP4):  K2 ←→ K5   (物理行0)
 *   Col3 (GP5):  K6 ←→ K9   (物理行1)
 *   Col4 (GP6):  K7 ←→ K10  (物理行1)
 *   Col5 (GP7):  K8 ←→ K11  (物理行1)
 *   Col6 (GP8):  K12 ←→ K15 (物理行2)
 *   Col7 (GP9):  K13 ←→ K16 (物理行2)
 *   Col8 (GP10): K14 ←→ K17 (物理行2)
 *   Col9 (GP11): K18 ←→ K21 (物理行3)
 *   Col10(GP12): K19 ←→ K22 (物理行3)
 *   Col11(GP13): K20 ←→ K23 (物理行3)
 *   Col12(GP14): K24 ←→ K27 (物理行4)
 *   Col13(GP15): K25 ←→ K28 (物理行4)
 *   Col14(GP16): K26 ←→ K29 (物理行4)
 * 
 * 线性键（Row2，独立 GPIO）：
 *   GP17, GP18, GP19, GP20, GP21, GP22
 */

#include "quantum.h"

// 矩阵行引脚（2根）
static const pin_t row_pins[] = { GP1, GP2 };
#define MATRIX_ROW_COUNT 2

// 矩阵列引脚（15根）
// 按物理行顺序：行0→行1→行2→行3→行4
// 每行内按列组：(列0-3), (列1-4), (列2-5)
static const pin_t col_pins[] = { 
    GP3,  GP8,  GP13,   // 物理行0: K0-K3, K1-K4, K2-K5
    GP4,  GP9,  GP14,   // 物理行1: K6-K9, K7-K10, K8-K11
    GP5,  GP10, GP15,   // 物理行2: K12-K15, K13-K16, K14-K17
    GP6,  GP11, GP16,   // 物理行3: K18-K21, K19-K22, K20-K23
    GP7,  GP12, GP17    // 物理行4: K24-K27, K25-K28, K26-K29
};
#define MATRIX_COL_COUNT 15

// 线性键引脚（6根，作为逻辑第3行）
static const pin_t direct_pins[] = { GP23, GP22, GP21, GP20, GP19, GP18 };
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
