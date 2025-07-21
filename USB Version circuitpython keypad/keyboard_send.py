import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)


def press_keys(keys):
    if keys is None:
        return

    if isinstance(keys, tuple):
        for key in keys:
            if key is not None:
                kbd.press(key)
    else:
        kbd.press(keys)


def release_keys(keys):
    if keys is None:
        return

    if isinstance(keys, tuple):
        for key in keys:
            if key is not None:
                kbd.release(key)
    else:
        kbd.release(keys)


def release_all_keys():
    kbd.release_all()
