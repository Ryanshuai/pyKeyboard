# 0.1 创建环境并安装
mamba create -n qmk python=3.11 -y
mamba activate qmk
pip install qmk
sudo apt install gcc-arm-none-eabi -y

# 0.2. 克隆 vial-qmk（如果还没有）
cd ~
git clone https://github.com/vial-kb/vial-qmk.git
cd vial-qmk
git submodule update --init --recursive



# 1. 复制文件到
mkdir -p ~/vial-qmk/keyboards/elf
cd ~/vial-qmk/keyboards/elf
cp -r elf_2x15_right ~/vial-qmk/keyboards/elf/elf_2x15_right

# 2. 编译，结果在 ~vial-qmk 下
cd ~/vial-qmk
make elf/elf_2x15_right:vial

# 3. 按住 boot 键，插入 use-b, 这样会弹出 Pico U盘。
# 复制 编译好的 uf.2 文件到  Pico U盘


