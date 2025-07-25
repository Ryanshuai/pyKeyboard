import time
import board
import keypad
import microcontroller

from keyboard_send import press_keys, release_keys, send_keys, release_all_keys
from configs import left_mat_pos_to_key, right_mat_pos_to_key, lin_key

mat_pos_to_key = right_mat_pos_to_key

time.sleep(1)
KEY_PINS = (board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17)
linear_keys = keypad.Keys(KEY_PINS, value_when_pressed=False, pull=True)
mat_keys = keypad.KeyMatrix(
    row_pins=(board.GP1, board.GP2, board.GP3, board.GP4, board.GP5),
    column_pins=(board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11),
)

fn = 0
while True:
    linear_event = linear_keys.events.get()
    mat_event = mat_keys.events.get()

    if linear_event:
        if linear_event.pressed:
            if linear_event.key_number == 0:
                fn = 1
            elif linear_event.key_number == 5:
                fn = 2
            else:
                press_keys(lin_key[linear_event.key_number])
        if linear_event.released:
            if linear_event.key_number == 0 or linear_event.key_number == 5:
                fn = 0
                release_all_keys()
            else:
                release_keys(lin_key[linear_event.key_number])

    if mat_event:
        if mat_event.pressed:
            press_keys(mat_pos_to_key[fn][mat_event.key_number])

        if mat_event.released:
            release_keys(mat_pos_to_key[fn][mat_event.key_number])

