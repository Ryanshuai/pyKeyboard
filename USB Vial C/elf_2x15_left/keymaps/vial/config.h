#pragma once

// Vial 唯一标识符
#define VIAL_KEYBOARD_UID {0xE1, 0xF0, 0x21, 0x4C, 0x45, 0x46, 0x54, 0x21}

// 解锁组合键
// Vial 界面显示第1行第3、4个键（蓝色高亮）
// vial.json keymap 第1行: ["0,0", "0,1", "0,2", "1,0", "1,1", "1,2"]
// 第3个键 = [0,2], 第4个键 = [1,0]
#define VIAL_UNLOCK_COMBO_ROWS {0, 1}
#define VIAL_UNLOCK_COMBO_COLS {2, 0}

// 动态层数
#define DYNAMIC_KEYMAP_LAYER_COUNT 4
