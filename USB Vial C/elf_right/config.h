#pragma once

// ============ 可定制选项 ============

// 双击 Reset 进入 Bootloader
#define RP2040_BOOTLOADER_DOUBLE_TAP_RESET
#define RP2040_BOOTLOADER_DOUBLE_TAP_RESET_TIMEOUT 200U  // 毫秒

// 矩阵大小
#define MATRIX_ROWS 6
#define MATRIX_COLS 6

// 防抖时间（毫秒），按键不灵敏可以调小，误触可以调大
#define DEBOUNCE 5
