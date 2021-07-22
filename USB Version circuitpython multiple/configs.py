from adafruit_hid.keycode import Keycode

# https://circuitpython.readthedocs.io/projects/hid/en/latest/_modules/adafruit_hid/keycode.html

lin_key = ["Fn2", Keycode.SHIFT, "Win", "Alt", "Ctrl", "Fn1"]

left_nml = [["", "", Keycode.TWO, Keycode.THRE, Keycode.FOUR, Keycode.FIVE],
            [Keycode.GRAVE_ACCENT, Keycode.ONE, "w", "e", "r", "t"],
            ["+", "q", "s", "d", "f", "g"],
            ["-", "a", "x", "c", "v", "b"],
            ["Esc", "z", "Backspace", "Space", "Enter", "Tab"]]
left_fn1 = [["", "", Keycode.F3, Keycode.F4, Keycode.F5, Keycode.F6],
            [Keycode.F1, Keycode.F2, "w", "<", ">", "'"],
            ["+", "q", "s", "(", ")", '"'],
            ["-", "a", "x", "[", "]", ":"],
            ["Esc", "z", "Backspace", "{", "}", ";"]]
left_fn2 = [["", "", "F3", "F4", "F5", "F6"],
            ["F1", "F2", "w", "e", "r", "t"],
            ["+", "q", "s", "d", "f", "g"],
            ["-", "a", "x", "c", "v", "b"],
            ["Esc", "z", "Backspace", "Space", "Enter", "Tab"]]

right_nml = [["6", "7", "8", "9", "", ""],
             ["y", "u", "i", "o", "0", Keycode.DELETE],
             ["h", "j", "k", "l", "p", "\\"],
             ["n", "m", "Up", ".", ",", "_", ],
             ["=", "Left", "Down", "Right", "*", "/"]]
right_fn1 = [["F7", "F8", "F9", "F10", "", ""],
             ["'", "<", ">", "o", "F11", "F12"],
             ['"', "(", ")", "l", "p", "\\"],
             [":", "[", "PgUp", ".", ",", "_", ],
             [";", "Home", "PgDown", "End", "*", "/"]]
right_fn2 = [["F7", "F8", "F9", "F10", "", ""],
             ["y", "u", "i", "o", "F11", "F12"],
             ["h", "j", "k", "l", "p", "\\"],
             ["n", "m", "Up", ".", ",", "_", ],
             ["=", "Left", "Down", "Right", "*", "/"]]

left_to_mat_key_names = [left_nml, left_fn1, left_fn2]
right_to_mat_key_names = [right_nml, right_fn1, right_fn2]
