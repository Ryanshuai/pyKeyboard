import board, digitalio, storage, usb_cdc, usb_hid, time

# 1. 按键接 GP12，上拉
button = digitalio.DigitalInOut(board.GP12)
button.switch_to_input(pull=digitalio.Pull.UP)

# 2. 禁用所有 USB 设备，确保接口数量可控
storage.disable_usb_drive()     # 不显示 U 盘 :contentReference[oaicite:0]{index=0}
usb_cdc.disable()               # 禁用串口
usb_hid.disable()               # 禁用所有 HID

# 给主机一点时间识别设备断开/重连
time.sleep(1.0)

# 3. 根据按键决定是否重新启用 U 盘（MSC）和串口（CDC）
if not button.value:
    # 按键未按下：显示 U 盘 + 串口
    storage.enable_usb_drive()  # 显示 CIRCUITPY 盘 :contentReference[oaicite:1]{index=1}
    usb_cdc.enable()            # 启用 USB-串口
else:
    # 按键按下：隐藏 U 盘 + 串口（只留键盘）
    storage.disable_usb_drive()
    usb_cdc.disable()

# 4. 最后启用键盘 HID（boot_device=1）
usb_hid.enable((usb_hid.Device.KEYBOARD,), boot_device=True)