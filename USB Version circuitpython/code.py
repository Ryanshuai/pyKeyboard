import time
import board

from keyboard_send import press_keys, release_keys, send_keys
from pyboard_io import LinearIO, MatrixIO
from keyboard_send import kbd, layout

from configs import left_to_mat_key_names, right_to_mat_key_names, lin_key

to_mat_keys = left_to_mat_key_names
lin_io = LinearIO([board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17])
mat_io = MatrixIO([board.GP1, board.GP2, board.GP3, board.GP4, board.GP5],
                  [board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11])

state_keys_previous = set()
mat_keys_previous = set()

while True:
    lin_pushed = lin_io.update()
    mat_pushed = mat_io.update()
    if len(lin_pushed) + len(mat_pushed) + len(state_keys_previous) + len(mat_keys_previous):
        state_keys = {lin_key[pos] for pos in lin_pushed}
        fn_num = ("Fn1" in state_keys)  # + 2 * ("fn2" in state_keys)
        state_keys.discard("Fn1")
        state_keys.discard("Fn2")
        mat_keys = {to_mat_keys[fn_num][pos[0]][pos[1]] for pos in mat_pushed}

        print("-----------------------")
        print(state_keys, state_keys_previous)
        press_keys(state_keys - state_keys_previous)
        release_keys(state_keys_previous - state_keys)

        print(mat_keys, mat_keys_previous)
        press_keys(mat_keys - mat_keys_previous)
        release_keys(mat_keys_previous - mat_keys)

        state_keys_previous = state_keys
        mat_keys_previous = mat_keys

        time.sleep(0.001)
