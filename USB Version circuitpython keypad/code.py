import time
import board
import keypad

from keyboard_send import press_keys, release_keys, release_all_keys
from configs import left_mat_pos_to_key, right_mat_pos_to_key, lin_key
from adafruit_hid.keycode import Keycode

mat_pos_to_key = left_mat_pos_to_key

time.sleep(0.1)
KEY_PINS = (board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17)
linear_keys = keypad.Keys(KEY_PINS, value_when_pressed=False, pull=True)
mat_keys = keypad.KeyMatrix(
    row_pins=(board.GP1, board.GP2, board.GP3, board.GP4, board.GP5),
    column_pins=(board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11),
)

release_all_keys()

fn = 0
shift_state = False
while True:
    linear_event = linear_keys.events.get()
    mat_event = mat_keys.events.get()

    # 行键区事件
    if linear_event:
        key = lin_key[linear_event.key_number]
        if linear_event.pressed:
            # Fn1 切换层
            if key == "Fn1":
                fn = 1
            # Shift 手动按下
            elif key == Keycode.SHIFT:
                shift_state = True
                press_keys(Keycode.SHIFT)
            else:
                press_keys(key)
        if linear_event.released:
            if key == "Fn1":
                fn = 0
                release_all_keys()
            elif key == Keycode.SHIFT:
                shift_state = False
                release_keys(Keycode.SHIFT)
            else:
                release_keys(key)

    # 矩阵区事件
    if mat_event:
        mapping = mat_pos_to_key[fn][mat_event.key_number]
        # 如果已手动按下 Shift，剔除映射中的 Shift
        if shift_state and isinstance(mapping, tuple):
            mapping = tuple(k for k in mapping if k is not Keycode.SHIFT)
        if mat_event.pressed:
            press_keys(mapping)
        if mat_event.released:
            release_keys(mapping)
