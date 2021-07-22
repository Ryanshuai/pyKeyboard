import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
# layout = KeyboardLayoutUS(kbd)
# layout.write('abc\n')
# keycodes = layout.keycodes('$')


kbd = Keyboard(usb_hid.devices)


# kbd.send(Keycode.SHIFT, Keycode.A)
# kbd.press(Keycode.TWO)
# kbd.release_all()


def press_keys(keys):
    for key in keys:
        if isinstance(key, tuple):
            kbd.press(*key)
        else:
            kbd.press(key)


def release_keys(keys):
    for key in keys:
        if isinstance(key, tuple):
            kbd.release(*key)
        else:
            kbd.release(key)


def release_all_keys():
    kbd.release_all()
