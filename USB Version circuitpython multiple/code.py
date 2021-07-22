import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode



# from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
# layout = KeyboardLayoutUS(kbd)
# layout.write('abc\n')
# keycodes = layout.keycodes('$')


kbd = Keyboard(usb_hid.devices)

from pyboard_io import LinearIO, MatrixIO
from user_setting_keys import left_to_mat_key_names, right_to_mat_key_names, lin_key
from send_keys import press_keys, release_all_keys

to_mat_keys = left_to_mat_key_names
lin_io = LinearIO([board.GP13, board.GP12, "B15", "A8", "A9", "A10"])
mat_io = MatrixIO(["A0", "A1", "A2", "A3", "A4"], ["B8", "B7", "B6", "B5", "B4", "B3"])

# to_mat_keys = right_to_mat_key_names
# lin_io = LinearIO([board.GP13, board.GP13, "B15", "A8", "A9", "A10"])
# mat_io = MatrixIO(["A0", "A1", "A2", "A3", "A4"], ["B0", "B1", "A7", "B3", "B4", "B5"])

time.sleep(1)  # wait for configuration

while True:
    lin_pushed = lin_io.update()
    mat_pushed = mat_io.update()
    if len(lin_pushed) + len(mat_pushed):
        state_keys = {lin_key[pos] for pos in lin_pushed}
        fn_num = ("Fn1" in state_keys) + 2 * ("fn2" in state_keys)
        state_keys.discard("Fn1")
        state_keys.discard("Fn2")
        mat_keys = {to_mat_keys[fn_num][pos[0]][pos[1]] for pos in mat_pushed}




    if len(lin_pushed) + len(mat_pushed):
        # print(lin_pushed, end=" ")

        fn_num = ("Fn1" in state_keys)  # + 2 * ("fn2" in state_keys)
        mat_keys = [to_mat_keys[fn_num][pos[0]][pos[1]] for pos in mat_pushed]
        print(state_keys, mat_keys)
        press_keys(state_keys, mat_keys)
        anyKeyPushed = 5
    elif anyKeyPushed > 0:
        release_keys()
        anyKeyPushed -= 1
    pyb.udelay(10)

pin13 = digitalio.DigitalInOut(board.GP13)
pin13.switch_to_input(pull=digitalio.Pull.UP)
print(pin13.value)

pin14 = digitalio.DigitalInOut(board.GP14)
pin14.switch_to_output(DriveMode=digitalio.DriveMode.OPEN_DRAIN)
print(pin14.value)

pin13 = digitalio.DigitalInOut(board.GP13)
pin13.switch_to_input(pull=digitalio.Pull.UP)
print(pin13.value)

pin14 = digitalio.DigitalInOut(board.GP14)
pin14.switch_to_output(DriveMode=digitalio.DriveMode.OPEN_DRAIN)
print(pin14.value)

kbd = Keyboard(usb_hid.devices)

# define buttons. these can be any physical switches/buttons, but the values
# here work out-of-the-box with a CircuitPlayground Express' A and B buttons.

# while True:
#     # press ALT+TAB to swap windows
#     kbd.send(Keycode.A)
#     time.sleep(1)
#     kbd.release_all()

# Type lowercase 'a'. Presses the 'a' key and releases it.
kbd.send(Keycode.A)

# Type capital 'A'.
kbd.send(Keycode.SHIFT, Keycode.A)

# Type control-x.
kbd.send(Keycode.CONTROL, Keycode.X)

# You can also control press and release actions separately.
kbd.press(Keycode.CONTROL, Keycode.X)
kbd.release_all()

# Press and hold the shifted '1' key to get '!' (exclamation mark).
kbd.press(Keycode.SHIFT, Keycode.ONE)
# Release the ONE key and send another report.
kbd.release(Keycode.ONE)
# Press shifted '2' to get '@'.
kbd.press(Keycode.TWO)
# Release all keys.
kbd.release_all()
