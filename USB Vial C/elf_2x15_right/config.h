#pragma once

// 双击 Reset 进入 Bootloader
#define RP2040_BOOTLOADER_DOUBLE_TAP_RESET
#define RP2040_BOOTLOADER_DOUBLE_TAP_RESET_TIMEOUT 200U

// 矩阵大小：2行矩阵 + 1行线性键 = 3行，15列
#define MATRIX_ROWS 3
#define MATRIX_COLS 15

// 防抖时间（毫秒）
#define DEBOUNCE 5
