# -*- coding: utf-8 -*-

lin_key_left = ["Esc", "Alt", "Fn2", "Fn1", "Win", "Space"]
lin_key_right = ["Esc", ("Ctrl", "Shift"), "Fn2", "Fn1", "Space", "Space"]

left_nml = [["", "", "2", "3", "4", "5"],
            ["1", "q", "w", "e", "r", "t"],
            ["Tab", "a", "s", "d", "f", "g"],
            ["Caps_Lock", "z", "x", "c", "v", "b"],
            ["Ctrl", ("(", ")", "Left"), "Shift", ("[", "]", "Left"), "F1", "F5"]]
left_fn1 = [["", "", "@", "#", "$", "%"],
            ["`", "q", "w", "e", "r", "t"],
            ["Tab", "a", "s", "d", "f", "g"],
            ["Caps_Lock", "z", "x", "c", "v", "b"],
            ["Ctrl",("(", ")", "Left"), "Shift", ("{", "}", "Left"), "F1", "F5"]]
left_fn2 = [["", "", "F2", "F3", "F4", "F5"],
            ["F1", "q", "w", "e", "r", "t"],
            ["Tab", "a", "s", "d", "f", "g"],
            ["Caps_Lock", "z", "x", "c", "v", "b"],
            ["Ctrl", ("(", ")", "Left"), "Shift", ("[", "]", "Left"), "F1", "F5"]]

right_nml = [["6", "7", "8", "9", "", ""],
             ["y", "u", "i", "o", "p", "Backspace"],
             ["h", "j", "k", "l", ";", "Enter"],
             ["n", "m", ",", ".", "?", ('"', '"', "Left"), ],
             ["0", "&", "*", "|", "Ins", ("Ctrl", "Alt")]]
right_fn1 = [["^", "F7", "F8", "F9", "", ""],
             ["+", "-", "Up", "=", "_", "Backspace"],
             ["h", "Left", "Down", "Right", ":", "Enter"],
             ["n", "m", "<", ">", "/", ("'", "'", "Left"), ],
             ["!", "&", "*", "|", "Del", ("Ctrl", "Alt")]]
right_fn2 = [["F6", "F7", "F8", "F9", "", ""],
             ["y", "u", "i", "o", "p", "Backspace"],
             ["h", "j", "k", "l", ";", "Enter"],
             ["n", "m", ",", ".", "?", ('"', '"', "Left"), ],
             ["0", "&", "*", "|", "Ins", ("Ctrl", "Alt")]]

left_to_mat_key_names = [left_nml, left_fn1, left_fn2]
right_to_mat_key_names = [right_nml, right_fn1, right_fn2]