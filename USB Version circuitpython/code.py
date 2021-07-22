import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard

from pyboard_io import LinearIO, MatrixIO
from user_setting_keys import left_to_mat_key_names, right_to_mat_key_names, lin_key

to_mat_keys = left_to_mat_key_names
lin_io = LinearIO([board.GP13, board.GP12, "B15", "A8", "A9", "A10"])
mat_io = MatrixIO(["A0", "A1", "A2", "A3", "A4"], ["B8", "B7", "B6", "B5", "B4", "B3"])

# to_mat_keys = right_to_mat_key_names
# lin_io = LinearIO([board.GP13, board.GP13, "B15", "A8", "A9", "A10"])
# mat_io = MatrixIO(["A0", "A1", "A2", "A3", "A4"], ["B0", "B1", "A7", "B3", "B4", "B5"])

kbd = Keyboard(usb_hid.devices)
state_keys_previous = set()
mat_keys_previous = set()

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

        kbd.press(state_keys - state_keys_previous)
        kbd.press(mat_keys - mat_keys_previous)

        kbd.release(state_keys_previous - state_keys)
        kbd.release(mat_keys_previous - mat_keys)
