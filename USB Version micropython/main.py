import pyb

from user_setting_keys import left_to_mat_key_names, right_to_mat_key_names, lin_key
from pyboard_io import LinearIO, MatrixIO
from send_keys import press_keys, release_keys

report_count = 10000 * 100
anyKeyPushed = 0

to_mat_keys = left_to_mat_key_names
lin_io = LinearIO(["B13", "B14", "B15", "A8", "A9", "A10"])
mat_io = MatrixIO(["A0", "A1", "A2", "A3", "A4"], ["B8", "B7", "B6", "B5", "B4", "B3"])

# to_mat_keys = right_to_mat_key_names
# lin_io = LinearIO(["B13", "B14", "B15", "A8", "A9", "A10"])
# mat_io = MatrixIO(["A0", "A1", "A2", "A3", "A4"], ["B0", "B1", "A7", "B3", "B4", "B5"])

pyb.delay(1000)  # wait for configuration

while True:
    for i in range(report_count):
        lin_io.update()
        mat_io.update()
        lin_pushed = lin_io.pushed()
        mat_pushed = mat_io.pushed()[:6]

        if len(lin_pushed) + len(mat_pushed):
            # print(lin_pushed, end=" ")
            state_keys = [lin_key[pos] for pos in lin_pushed]
            fn_num = ("Fn1" in state_keys)  # + 2 * ("fn2" in state_keys)
            mat_keys = [to_mat_keys[fn_num][pos[0]][pos[1]] for pos in mat_pushed]
            print(state_keys, mat_keys)
            press_keys(state_keys, mat_keys)
            anyKeyPushed = 5
        elif anyKeyPushed > 0:
            release_keys()
            anyKeyPushed -= 1
        pyb.udelay(10)
    release_keys()
