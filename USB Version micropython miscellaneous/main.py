# -*- coding: utf-8 -*-
import pyb

from user_setting_keys import left_to_mat_key_names, right_to_mat_key_names, lin_key_left, lin_key_right
from pyboard_io import LinearIO, MatrixIO
from send_keys import press_keys, release_keys

report_count = 10000 * 100
anyKeyPushed = 0

lin_key = lin_key_left
to_mat_keys = left_to_mat_key_names

# lin_key = lin_key_right
# to_mat_keys = right_to_mat_key_names
lin_io = LinearIO(["B13", "B14", "B15", "A8", "A9", "A10"])
mat_io = MatrixIO(["A0", "A1", "A2", "A3", "A4"], ["B3", "B4", "B5", "B6", "B7", "B8"])

pyb.delay(1000)  # wait for configuration

while True:
    for i in range(report_count):
        lin_io.update()
        mat_io.update()
        lin_pushed = lin_io.pushed()
        mat_pushed = mat_io.pushed()[:6]

        if len(lin_pushed) + len(mat_pushed):
            # print(lin_pushed, end=" ")
            state_keys = list()
            for pos in lin_pushed:
                state_key = lin_key[pos]
                if isinstance(state_key, list):
                    state_keys += state_key
                else:
                    state_keys.append(state_key)

            fn_num = 0
            if "Fn2" in state_keys:
                fn_num = 2
            if "Fn1" in state_keys:
                fn_num = 1

            mat_keys = list()
            for pos in mat_pushed:
                mat_key = to_mat_keys[fn_num][pos[0]][pos[1]]
                if isinstance(mat_key, list):
                    state_keys += mat_key
                else:
                    state_keys.append(mat_key)

            print(state_keys, mat_keys)
            press_keys(state_keys, mat_keys)
            anyKeyPushed = 5
        elif anyKeyPushed > 0:
            release_keys()
            anyKeyPushed -= 1
        pyb.udelay(10)
    release_keys()
