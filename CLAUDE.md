# pyKeyboard

自制**分体键盘**(左右两半独立,STM32F411 / CircuitPython / MicroPython / Vial-C 多版本固件)。

## 已知坑:Linux 下中文输入卡顿(慢半拍)

**现象**:在 Linux 上用输入法(fcitx5 / ibus 等)打中文时,快速打字会觉得中文"不实时、慢半拍",但打英文完全跟手。

**原因**:分体键盘的左右两半在系统里是**两个独立的键盘设备**(`xinput list` 能看到 `... Left Keyboard` 和 `... Right Keyboard` 两个)。打拼音时字母在左右手交替 = 按键事件在两个设备间交替到达,会打断输入法的拼音组字;英文不走组字所以无感。**不是输入法的问题,别在输入法框架上瞎折腾。**

**解决**:用 [keyd](https://github.com/rvaiya/keyd) 在最底层把所有物理键盘合并成**一个虚拟键盘**,输入法只看到一个设备,冲突消失。

```bash
# 1. 编译安装(apt 源里没有 keyd)
sudo apt install -y build-essential git
git clone https://github.com/rvaiya/keyd && cd keyd && make && sudo make install

# 2. 纯合并、不改任何键的配置
sudo mkdir -p /etc/keyd
printf '[ids]\n*\n\n[main]\n' | sudo tee /etc/keyd/default.conf

# 3. 启用(立即生效,开机自启)
sudo systemctl enable --now keyd
```

启用后在分体键盘上打中文即恢复跟手。

> 若合并后仍卡,才可能是左右两半**无线同步延迟**导致字母乱序,那需从固件侧调(降低分体同步延迟 / 让某一半作为唯一主机上报)。
