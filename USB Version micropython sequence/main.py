# -*- coding: utf-8 -*-

import pyb

from user_setting_keys import left_to_mat_key_names, right_to_mat_key_names, lin_key_left, lin_key_right
from pyboard_io import LinearIO, MatrixIO
from send_keys import Sender, release_keys

sender = Sender()
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
            print(lin_pushed, mat_pushed)
            state_keys = [lin_key[pos] for pos in lin_pushed]
            fn_num = "Fn1" in state_keys
            if "Fn2" in state_keys:
                fn_num = 2
            mat_keys = [to_mat_keys[fn_num][pos[0]][pos[1]] for pos in mat_pushed]

            sender.decode_keys(state_keys + mat_keys)
            sender.send_buffers()
            anyKeyPushed = 5
        elif anyKeyPushed > 0:
            release_keys()
            anyKeyPushed -= 1

    release_keys()
