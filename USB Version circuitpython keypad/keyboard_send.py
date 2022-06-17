import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# keycodes = layout.keycodes('$')
# kbd.send(Keycode.SHIFT, Keycode.A)
# kbd.press(Keycode.TWO)
# kbd.release_all()

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)


def send_keys(keys):
    for key in keys:
        if isinstance(key, str):
            layout.write(key)
        elif isinstance(key, tuple):
            kbd.send(*key)
        else:
            kbd.send(key)


def press_keys(keys):
    if isinstance(keys, int):
        kbd.press(keys)
    elif isinstance(keys, str):
        keys = layout.keycodes(keys)
        press_keys(keys)
    else:
        for key in keys:
            press_keys(key)


def release_keys(keys):
    if isinstance(keys, int):
        kbd.release(keys)
    elif isinstance(keys, str):
        keys = layout.keycodes(keys)
        release_keys(keys)
    else:
        for key in keys:
            release_keys(key)


def release_all_keys():
    kbd.release_all()
