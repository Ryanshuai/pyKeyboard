from adafruit_hid.keycode import Keycode


lin_key = ("Fn1", Keycode.CONTROL, Keycode.ALT, Keycode.GUI, Keycode.SHIFT, (Keycode.CONTROL, Keycode.F8))

left_nml = (None, None, Keycode.TWO, Keycode.THREE, Keycode.FOUR, Keycode.FIVE,
            Keycode.GRAVE_ACCENT, Keycode.ONE, Keycode.W, Keycode.E, Keycode.R, Keycode.T,
            Keycode.KEYPAD_PLUS, Keycode.Q, Keycode.S, Keycode.D, Keycode.F, Keycode.G,
            Keycode.KEYPAD_MINUS, Keycode.A, Keycode.X, Keycode.C, Keycode.V, Keycode.B,
            Keycode.ESCAPE, Keycode.Z, Keycode.BACKSPACE, Keycode.SPACE, Keycode.ENTER, Keycode.TAB)
left_fn1 = (None, None, Keycode.F3, Keycode.F4, Keycode.F5, Keycode.F6,
            Keycode.F1, Keycode.F2, Keycode.W, (Keycode.SHIFT, Keycode.COMMA), (Keycode.SHIFT, Keycode.PERIOD),Keycode.QUOTE,
            Keycode.KEYPAD_PLUS, Keycode.Q, Keycode.S, (Keycode.SHIFT, Keycode.NINE), (Keycode.SHIFT, Keycode.ZERO),(Keycode.SHIFT, Keycode.QUOTE),
            Keycode.KEYPAD_MINUS, Keycode.A, Keycode.X, Keycode.LEFT_BRACKET, Keycode.RIGHT_BRACKET, Keycode.SEMICOLON,
            Keycode.ESCAPE, Keycode.Z, Keycode.BACKSPACE, (Keycode.SHIFT, Keycode.LEFT_BRACKET), (Keycode.SHIFT, Keycode.RIGHT_BRACKET), Keycode.SEMICOLON)

# left_fn2 = (None, None, Keycode.F3, Keycode.F4, Keycode.F5, Keycode.F6,
#             Keycode.F1, Keycode.F2, "w", "e", "r", "t",
#             Keycode.KEYPAD_PLUS, "q", (Keycode.CONTROL ,Keycode.F2), (Keycode.SHIFT ,Keycode.F9),  (Keycode.SHIFT ,Keycode.F10), "g",
#             Keycode.KEYPAD_MINUS, "a", Keycode.F9,(Keycode.ALT ,Keycode.F8), Keycode.F8, (Keycode.CONTROL ,Keycode.F8),
#             Keycode.ESCAPE, "z", Keycode.BACKSPACE, Keycode.SPACE, Keycode.ENTER, Keycode.TAB)

right_nml = (Keycode.SIX, Keycode.SEVEN, Keycode.EIGHT, Keycode.NINE, None, None,
             Keycode.Y, Keycode.U, Keycode.I, Keycode.O, Keycode.ZERO, Keycode.DELETE,
             Keycode.H, Keycode.J, Keycode.K, Keycode.L, Keycode.P, Keycode.BACKSLASH,
             Keycode.N, Keycode.M, Keycode.UP_ARROW, Keycode.PERIOD, Keycode.COMMA, (Keycode.SHIFT, Keycode.MINUS),
             Keycode.EQUALS, Keycode.LEFT_ARROW, Keycode.DOWN_ARROW, Keycode.RIGHT_ARROW, Keycode.KEYPAD_ASTERISK, Keycode.FORWARD_SLASH)
right_fn1 = (Keycode.F7, Keycode.F8, Keycode.F9, Keycode.F10, None, None,
             Keycode.QUOTE, (Keycode.SHIFT, Keycode.COMMA), (Keycode.SHIFT, Keycode.PERIOD), Keycode.O, Keycode.F11, Keycode.F12,
             (Keycode.SHIFT, Keycode.QUOTE), (Keycode.SHIFT, Keycode.NINE), (Keycode.SHIFT, Keycode.ZERO), Keycode.L, Keycode.P, Keycode.BACKSLASH,
             (Keycode.SHIFT, Keycode.SEMICOLON), (Keycode.SHIFT, Keycode.NINE), Keycode.PAGE_UP, Keycode.PERIOD, Keycode.COMMA, (Keycode.SHIFT, Keycode.MINUS),
             Keycode.SEMICOLON, Keycode.HOME, Keycode.PAGE_DOWN, Keycode.END, Keycode.KEYPAD_ASTERISK, (Keycode.SHIFT, Keycode.FORWARD_SLASH))
# right_fn2 = (Keycode.F7, Keycode.F8, Keycode.F9, Keycode.F10, None, None,
#              "y", "u", "i", "o", Keycode.F11, Keycode.F12,
#              "h", "j", "k", "l", "p", "\\",
#              "n", "m", Keycode.UP_ARROW, ".", ",", "_",
#              "=", Keycode.LEFT_ARROW, Keycode.DOWN_ARROW, Keycode.RIGHT_ARROW, "*", Keycode.FORWARD_SLASH)

left_mat_pos_to_key = (left_nml, left_fn1)
right_mat_pos_to_key = (right_nml, right_fn1)
