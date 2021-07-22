import time
import board

from keyboard_send import press_keys, release_keys, send_keys
from pyboard_io import LinearIO, MatrixIO
from keyboard_send import kbd, layout

from configs import left_to_mat_key_names, right_to_mat_key_names, lin_key


to_mat_keys = left_to_mat_key_names
lin_io = LinearIO([board.GP13, board.GP12, board.GP11, board.GP10, board.GP9, board.GP8, ])
mat_io = MatrixIO([board.GP7, board.GP6, board.GP5, board.GP4, board.GP3],
                  [board.GP22, board.GP21, board.GP20, board.GP2, board.GP1])

state_keys_previous = set()

time.sleep(1)  # wait for configuration

import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
test = left_to_mat_key_names[0]
for i in range(len(test)):
    for j in range(len(test[0])):
        led.value = 1 - led.value
        print(i, j, test[i][j])
        time.sleep(1)
        key = test[i][j]
        if isinstance(key, str):
            layout.write(key)
        elif isinstance(key, tuple):
            kbd.send(*key)
        else:
            kbd.send(key)

# while True:
#     lin_pushed = lin_io.update()
#     mat_pushed = mat_io.update()
#     if len(lin_pushed) + len(mat_pushed):
#         state_keys = {lin_key[pos] for pos in lin_pushed}
#         fn_num = ("Fn1" in state_keys)  # + 2 * ("fn2" in state_keys)
#         state_keys.discard("Fn1")
#         state_keys.discard("Fn2")
#         mat_keys = [to_mat_keys[fn_num][pos[0]][pos[1]] for pos in mat_pushed]
#
#         press_keys(*(state_keys - state_keys_previous))
#         release_keys(*(state_keys_previous - state_keys))
#
#         send_keys(mat_keys[:6])

