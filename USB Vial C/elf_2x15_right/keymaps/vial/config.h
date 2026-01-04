#pragma once

// Vial 唯一标识符
#define VIAL_KEYBOARD_UID {0xE1, 0xF0, 0x21, 0x52, 0x49, 0x47, 0x48, 0x54}

// 解锁组合键：同时按第一行中间两个键（8 和 9）
// vial.json keymap 第1行: ["0,0", "0,1", "0,2", "1,0", "1,1", "1,2"]
// 对应按键:               6      7      8      9     (空)   (空)
// 所以 8 = [0,2], 9 = [1,0]
#define VIAL_UNLOCK_COMBO_ROWS {0, 1}
#define VIAL_UNLOCK_COMBO_COLS {2, 0}

// 动态层数
#define DYNAMIC_KEYMAP_LAYER_COUNT 4
