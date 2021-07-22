from adafruit_hid.keycode import Keycode

# https://circuitpython.readthedocs.io/projects/hid/en/latest/_modules/adafruit_hid/keycode.html

lin_key = ["Fn2", Keycode.SHIFT, Keycode.WINDOWS, Keycode.ALT, Keycode.CONTROL, "Fn1"]

left_nml = [["", "", Keycode.TWO, Keycode.THREE, Keycode.FOUR, Keycode.FIVE],
            [Keycode.GRAVE_ACCENT, Keycode.ONE, "w", "e", "r", "t"],
            ["+", "q", "s", "d", "f", "g"],
            ["-", "a", "x", "c", "v", "b"],
            [Keycode.ESCAPE, "z", Keycode.BACKSPACE, Keycode.SPACE, Keycode.ENTER, Keycode.TAB]]
left_fn1 = [["", "", Keycode.F3, Keycode.F4, Keycode.F5, Keycode.F6],
            [Keycode.F1, Keycode.F2, "w", "<", ">", "'"],
            ["+", "q", "s", "(", ")", '"'],
            ["-", "a", "x", "[", "]", ":"],
            ["Esc", "z", Keycode.BACKSPACE, "{", "}", ";"]]
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
right_fn1 = [["F7", "F8", "F9", "F10", "", ""],
             ["'", "<", ">", "o", "F11", "F12"],
             ['"', "(", ")", "l", "p", "\\"],
             [":", "[", Keycode.PAGE_UP, ".", ",", "_", ],
             [";", Keycode.HOME, Keycode.PAGE_DOWN , Keycode.END, "*", "/"]]
right_fn2 = [["F7", "F8", "F9", "F10", "", ""],
             ["y", "u", "i", "o", "F11", "F12"],
             ["h", "j", "k", "l", "p", "\\"],
             ["n", "m", "Up", ".", ",", "_", ],
             ["=", "Left", "Down", "Right", "*", "/"]]

left_to_mat_key_names = [left_nml, left_fn1, left_fn2]
right_to_mat_key_names = [right_nml, right_fn1, right_fn2]
