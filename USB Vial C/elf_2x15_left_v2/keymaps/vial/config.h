#pragma once

// debug mode
//#define VIAL_INSECURE

// Vial 唯一标识符 (8 字节)
#define VIAL_KEYBOARD_UID {0xE1, 0xF0, 0x21, 0x4C, 0x45, 0x46, 0x54, 0x31}

// 解锁组合键：同时按第二行的第3、4个键
// vial.json keymap 第2行: ["0,3", "0,4", "0,5", "1,3", "1,4", "1,5"]
// 对应矩阵位置 [0,5] 和 [1,3]
#define VIAL_UNLOCK_COMBO_ROWS {0, 1}
#define VIAL_UNLOCK_COMBO_COLS {5, 3}

// 动态层数
#define DYNAMIC_KEYMAP_LAYER_COUNT 4
