#pragma once

// ============ Vial 定制选项 ============

// Vial 唯一标识符（每个键盘不同）
#define VIAL_KEYBOARD_UID {0xE1, 0xF0, 0x01, 0x52, 0x49, 0x47, 0x48, 0x54}

// 解锁组合键：同时按这两个键解锁 Vial
// 当前设置：按矩阵 [0,0] 和 [0,1] 位置的键（即 6 和 7）
#define VIAL_UNLOCK_COMBO_ROWS {0, 0}
#define VIAL_UNLOCK_COMBO_COLS {0, 1}

// 动态层数（Vial 中可用的层数）
#define DYNAMIC_KEYMAP_LAYER_COUNT 4
