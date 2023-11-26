import time
import board
import keypad

from keyboard_send import press_keys, release_keys
from configs import keys, fn_keys



time.sleep(1)
mat_keys = keypad.KeyMatrix(
    row_pins=(board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7,board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14,board.GP15, board.GP26, board.GP27, board.GP28),
    column_pins=(board.GP16, board.GP17, board.GP18, board.GP19, board.GP20),
)

fn = 0
while True:
    mat_event = mat_keys.events.get()

    if mat_event:
        if mat_event.pressed:
            print(mat_event.key_number)
            if mat_event.key_number == 0:
                fn = 1
            else:
                if fn == 0:
                    press_keys(keys[mat_event.key_number])
                else:
                    press_keys(fn_keys[mat_event.key_number])

        if mat_event.released:
            if mat_event.key_number == 0:
                fn = 0
            else:
                if fn == 0:
                    press_keys(keys[mat_event.key_number])
                else:
                    press_keys(fn_keys[mat_event.key_number])
