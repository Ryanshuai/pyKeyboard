# -*- coding: utf-8 -*-

import pyb

hid = pyb.USB_HID()


class Sender:
    def __init__(self):
        self.byte0 = 0
        self.normal_buff = set()
        self.shift_buff = set()
        self.sequence_buff = list()

    def decode_keys(self, keys):
        self.is_shift = False
        self.byte0 = 0
        self.normal_buff = set()
        self.shift_buff = set()
        self.sequence_buff = list()

        keys = set(keys)
        if "Ctrl" in keys:
            self.byte0 |= 1
        if "Alt" in keys:
            self.byte0 |= 4
        if "Win" in keys:
            self.byte0 |= 8

        if "Shift" in keys:
            self.byte0 |= 2
            for key in keys:
                if isinstance(key, tuple):
                    continue

                hex, b0 = key_to_hex.get(key, [0, 0])
                self.shift_buff.add(hex)
            self.shift_buff.discard(0)
            return

        for key in keys:
            if isinstance(key, tuple):
                self.sequence_buff = [key_to_hex.get(k, [0, 0]) for k in key]

            hex, b0 = key_to_hex.get(key, [0, 0])
            if b0 == 2:
                self.shift_buff.add(hex)
            else:
                self.normal_buff.add(hex)
            self.normal_buff.discard(0)
            self.shift_buff.discard(0)

    def send_buffers(self):
        if self.sequence_buff:
            for hex, byte0 in self.sequence_buff:
                press_keys(byte0, [hex])
                self.release_keys()
            self.release_keys(100)
            return

        if self.shift_buff:
            press_keys(self.byte0 | 2, self.shift_buff)
        else:
            press_keys(self.byte0, self.normal_buff)

    def release_keys(self, time=None):
        time = time if time else 10
        hid.send(bytearray(8))
        pyb.delay(time)


def press_keys(byte0, key_hex_codes):
    buf = bytearray(8)
    buf[0] = byte0

    i = 2
    for key_code in key_hex_codes:
        buf[i] = key_code
        i += 1

        if i > 5:
            break

    hid.send(buf)
    pyb.delay(10)


key_to_hex = {
    "a": [0x04, 0],
    "b": [0x05, 0],
    "c": [0x06, 0],
    "d": [0x07, 0],
    "e": [0x08, 0],
    "f": [0x09, 0],
    "g": [0x0A, 0],
    "h": [0x0B, 0],
    "i": [0x0C, 0],
    "j": [0x0D, 0],
    "k": [0x0E, 0],
    "l": [0x0F, 0],
    "m": [0x10, 0],
    "n": [0x11, 0],
    "o": [0x12, 0],
    "p": [0x13, 0],
    "q": [0x14, 0],
    "r": [0x15, 0],
    "s": [0x16, 0],
    "t": [0x17, 0],
    "u": [0x18, 0],
    "v": [0x19, 0],
    "w": [0x1A, 0],
    "x": [0x1B, 0],
    "y": [0x1C, 0],
    "z": [0x1D, 0],
    "_": [0x2D, 2],

    "Backspace": [0x2A, 0],
    "Space": [0x2C, 0],
    "Enter": [0x28, 0],
    "Tab": [0x2B, 0],
    "Esc": [0x29, 0],
    "Del": [0x4C, 0],
    "Ins": [0x49, 0],
    "Caps_Lock": [0x39, 0],
    "Num_Lock": [144, 0],
    "Mute": [0xef, 0],

    "Home": [74, 0],
    "End": [77, 0],
    "PgUp": [75, 0],
    "PgDown": [78, 0],

    "Up": [0x52, 0],
    "Down": [0x51, 0],
    "Left": [0x50, 0],
    "Right": [0x4F, 0],

    "`": [0x35, 0],
    "1": [0x1E, 0],
    "!": [0x1E, 2],
    "2": [0x1F, 0],
    "@": [0x1F, 2],
    "3": [0x20, 0],
    "#": [0x20, 2],
    "4": [0x21, 0],
    "$": [0x21, 2],
    "5": [0x22, 0],
    "%": [0x22, 2],
    "6": [0x23, 0],
    "^": [0x23, 2],
    "7": [0x24, 0],
    "&": [0x24, 2],
    "8": [0x25, 0],
    "9": [0x26, 0],
    "(": [0x26, 2],
    "0": [0x27, 0],
    ")": [0x27, 2],

    "=": [0x2E, 0],
    "+": [0x57, 0],
    "-": [0x56, 0],
    "*": [0x55, 0],
    "/": [0x54, 0],
    "|": [0x31, 2],

    "'": [0x34, 0],
    '"': [0x34, 2],
    "?": [0x38, 2],
    ",": [0x36, 0],
    "<": [0x36, 2],
    ".": [0x37, 0],
    ">": [0x37, 2],
    "\\": [0x64, 0],
    "[": [0x2F, 0],
    "{": [0x2F, 2],
    "]": [0x30, 0],
    "}": [0x30, 2],
    ";": [0x33, 0],
    ":": [0x33, 2],

    "F1": [0x3A, 0],
    "F2": [0x3B, 0],
    "F3": [0x3C, 0],
    "F4": [0x3D, 0],
    "F5": [0x3E, 0],
    "F6": [0x3F, 0],
    "F7": [0x40, 0],
    "F8": [0x41, 0],
    "F9": [0x42, 0],
    "F10": [0x43, 0],
    "F11": [0x44, 0],
    "F12": [0x45, 0],
}
