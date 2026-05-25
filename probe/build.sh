#!/usr/bin/env bash
# 一键构建 probe.uf2
# 依赖: git, cmake, ninja, arm-none-eabi-gcc
# 首次运行会自动 clone pico-sdk (~500MB)

set -e
cd "$(dirname "$0")"

# 1. 自动挂载 xpack ARM toolchain (若在 D:/50_tools/ 下)
if ! command -v arm-none-eabi-gcc >/dev/null 2>&1; then
    XPACK_BIN=$(ls -d /d/50_tools/xpack-arm-none-eabi-gcc-*/bin 2>/dev/null | head -1)
    if [ -n "$XPACK_BIN" ]; then
        export PATH="$XPACK_BIN:$PATH"
        echo "using toolchain at $XPACK_BIN"
    fi
fi

# 2. 检查工具链
for tool in git cmake ninja arm-none-eabi-gcc; do
    if ! command -v "$tool" >/dev/null 2>&1; then
        echo "ERROR: $tool not found in PATH" >&2
        echo "ARM toolchain: https://github.com/xpack-dev-tools/arm-none-eabi-gcc-xpack/releases" >&2
        exit 1
    fi
done

# 2. 拉 pico-sdk
SDK_DIR="${PICO_SDK_PATH:-$PWD/pico-sdk}"
if [ ! -d "$SDK_DIR/src" ]; then
    echo "[1/3] cloning pico-sdk to $SDK_DIR ..."
    git clone --depth 1 --recurse-submodules \
        https://github.com/raspberrypi/pico-sdk.git "$SDK_DIR"
else
    echo "[1/3] pico-sdk already present at $SDK_DIR"
fi
export PICO_SDK_PATH="$SDK_DIR"

# 3. 复制 pico_sdk_import.cmake (若尚未复制)
if [ ! -f pico_sdk_import.cmake ]; then
    cp "$SDK_DIR/external/pico_sdk_import.cmake" .
fi

# 4. cmake + ninja
# 5. 如有预编译 pico-sdk-tools, 把 picotool/pioasm 路径传给 cmake
# 避免 cmake 去 fetch 并编译它们 (需要主机 C 编译器)
PST="${PICO_SDK_TOOLS:-/d/50_tools/pico-sdk-tools}"
EXTRA_CMAKE=""
if [ -f "$PST/picotool/picotoolConfig.cmake" ]; then
    EXTRA_CMAKE+=" -Dpicotool_DIR=$PST/picotool"
    echo "using prebuilt picotool at $PST/picotool"
fi
if [ -f "$PST/pioasm/pioasmConfig.cmake" ]; then
    EXTRA_CMAKE+=" -Dpioasm_DIR=$PST/pioasm"
fi

echo "[2/3] cmake configure ..."
mkdir -p build
cd build
cmake -G Ninja -DPICO_BOARD=pico $EXTRA_CMAKE ..

echo "[3/3] building ..."
ninja

echo ""
echo "=========================="
echo "  OK: $(pwd)/probe.uf2"
echo "=========================="
