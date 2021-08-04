from adafruit_hid.keycode import Keycode

# lin_key = ["Fn2", Keycode.SHIFT, Keycode.WINDOWS, Keycode.ALT, Keycode.CONTROL, "Fn1"]
lin_key = ["Fn1", Keycode.CONTROL, Keycode.ALT, Keycode.WINDOWS, Keycode.SHIFT, "Fn2"]

left_nml = [[0, 0, Keycode.TWO, Keycode.THREE, Keycode.FOUR, Keycode.FIVE],
            [Keycode.GRAVE_ACCENT, Keycode.ONE, Keycode.W, Keycode.E, Keycode.R, Keycode.T],
            [Keycode.KEYPAD_PLUS, Keycode.Q, Keycode.S, Keycode.D, Keycode.F, Keycode.G],
            [Keycode.KEYPAD_MINUS, Keycode.A, Keycode.X, Keycode.C, Keycode.V, Keycode.B],
            [Keycode.ESCAPE, Keycode.Z, Keycode.BACKSPACE, Keycode.SPACE, Keycode.ENTER, Keycode.TAB]]
left_fn1 = [["", "", Keycode.F3, Keycode.F4, Keycode.F5, Keycode.F6],
            [Keycode.F1, Keycode.F2, "w", "<", ">", "'"],
            ["+", "q", "s", "(", ")", '"'],
            ["-", "a", "x", "[", "]", ":"],
            [Keycode.ESCAPE, "z", Keycode.BACKSPACE, "{", "}", ";"]]
left_fn2 = [["", "", Keycode.F3, Keycode.F4, Keycode.F5, Keycode.F6],
            [Keycode.F1, Keycode.F2, "w", "e", "r", "t"],
            ["+", "q", "s", "d", "f", "g"],
            ["-", "a", "x", "c", "v", "b"],
            [Keycode.ESCAPE, "z", Keycode.BACKSPACE, Keycode.SPACE, Keycode.ENTER, Keycode.TAB]]

right_nml = [[Keycode.SIX, Keycode.SEVEN, Keycode.EIGHT, Keycode.NINE, "", ""],
             ["y", "u", "i", "o", Keycode.ZERO, Keycode.DELETE],
             ["h", "j", "k", "l", "p", Keycode.BACKSLASH],
             ["n", "m", Keycode.UP_ARROW, ".", ",", "_", ],
             ["=", Keycode.LEFT_ARROW, Keycode.DOWN_ARROW, Keycode.RIGHT_ARROW, "*", Keycode.FORWARD_SLASH]]
right_fn1 = [[Keycode.F7, Keycode.F8, Keycode.F9, Keycode.F10, "", ""],
             ["'", "<", ">", "o", Keycode.F11, Keycode.F12],
             ['"', "(", ")", "l", "p", "\\"],
             [":", "[", Keycode.PAGE_UP, ".", ",", "_", ],
             [";", Keycode.HOME, Keycode.PAGE_DOWN, Keycode.END, "*", "/"]]
right_fn2 = [[Keycode.F7, Keycode.F8, Keycode.F9, Keycode.F10, "", ""],
             ["y", "u", "i", "o", Keycode.F11, Keycode.F12],
             ["h", "j", "k", "l", "p", "\\"],
             ["n", "m", Keycode.UP_ARROW, ".", ",", "_", ],
             ["=", Keycode.LEFT_ARROW, Keycode.DOWN_ARROW, Keycode.RIGHT_ARROW, "*", Keycode.FORWARD_SLASH]]

left_to_mat_key_names = [left_nml, left_fn1, left_fn2]
right_to_mat_key_names = [right_nml, right_fn1, right_fn2]
