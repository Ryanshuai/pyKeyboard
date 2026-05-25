cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(probe C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

pico_sdk_init()

add_executable(probe main.c)

# 生成 toggle.pio.h
pico_generate_pio_header(probe ${CMAKE_CURRENT_LIST_DIR}/toggle.pio)

target_link_libraries(probe pico_stdlib hardware_pio hardware_timer)

# 启用 USB CDC 作为 stdio
pico_enable_stdio_usb(probe 1)
pico_enable_stdio_uart(probe 0)

pico_add_extra_outputs(probe)
