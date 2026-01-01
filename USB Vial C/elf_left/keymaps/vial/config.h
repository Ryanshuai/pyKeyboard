#pragma once

// ============ Vial 定制选项 ============

// Vial 唯一标识符（每个键盘不同）
#define VIAL_KEYBOARD_UID {0xE1, 0xF0, 0x02, 0x4C, 0x45, 0x46, 0x54, 0x21}

// 解锁组合键：同时按这两个键解锁 Vial
// 当前设置：按矩阵 [0,2] 和 [0,3] 位置的键（即 2 和 3）
#define VIAL_UNLOCK_COMBO_ROWS {0, 0}
#define VIAL_UNLOCK_COMBO_COLS {2, 3}

// 动态层数（Vial 中可用的层数）
#define DYNAMIC_KEYMAP_LAYER_COUNT 4
