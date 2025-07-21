import storage, usb_cdc
import usb_hid
import board, digitalio
import time

# In this example, the button is wired to connect GP12 to +V when pushed.
button = digitalio.DigitalInOut(board.GP12)
button.switch_to_input(pull=digitalio.Pull.UP)

# Disable USB storage and CDC only if the button is not pressed.
if button.value:
    storage.disable_usb_drive()
    usb_cdc.disable()

# —— 强制 USB HID 重枚举 ——
time.sleep(0.1)  # 等待接口关闭
usb_hid.disable()  
time.sleep(0.1)  # 给主机感知总线变化
usb_hid.enable(
    (usb_hid.Device.KEYBOARD,),  # 只启用键盘接口
    boot_device=True             # 让它作为第一个接口重新枚举
)
