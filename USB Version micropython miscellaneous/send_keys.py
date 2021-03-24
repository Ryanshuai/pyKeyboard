# -*- coding: utf-8 -*-

import pyb

hid = pyb.USB_HID()


def decode_keys(state_keys, mat_keys):
    all_keys = state_keys + mat_keys

    all_keys = set(all_keys)

    byte0 = 0
    if "Ctrl" in all_keys:
        byte0 |= 1
    if "Shift" in all_keys:
        byte0 |= 2
    if "Alt" in all_keys:
        byte0 |= 4
    if "Win" in all_keys:
        byte0 |= 8

    key_hex_codes = set()
    for key in all_keys:
        if isinstance(key, list):
            key_hex_codes = list()
            for k in key:
                hex = key_to_hex.get(k, 0)
                if isinstance(hex, list):
                    hex = hex[0]
                    byte0 |= 2
                key_hex_codes.append(hex)
            return byte0, key_hex_codes

        hex = key_to_hex.get(key, 0)
        if isinstance(hex, list):
            hex = hex[0]
            byte0 |= 2
        key_hex_codes.add(hex)

    key_hex_codes.discard(0)
    return byte0, key_hex_codes


def press_keys(state_keys, mat_keys):
    byte0, key_hex_codes = decode_keys(state_keys, mat_keys)
    buf = bytearray(8)
    buf[0] = byte0

    i = 2
    for key_code in key_hex_codes:
        buf[i] = key_code
        i += 1

    hid.send(buf)
    pyb.delay(10)


def release_keys():
    hid.send(bytearray(8))
    pyb.delay(10)


key_to_hex = {
    "a": 0x04,
    "b": 0x05,
    "c": 0x06,
    "d": 0x07,
    "e": 0x08,
    "f": 0x09,
    "g": 0x0A,
    "h": 0x0B,
    "i": 0x0C,
    "j": 0x0D,
    "k": 0x0E,
    "l": 0x0F,
    "m": 0x10,
    "n": 0x11,
    "o": 0x12,
    "p": 0x13,
    "q": 0x14,
    "r": 0x15,
    "s": 0x16,
    "t": 0x17,
    "u": 0x18,
    "v": 0x19,
    "w": 0x1A,
    "x": 0x1B,
    "y": 0x1C,
    "z": 0x1D,
    "_": [0x2D],

    "Backspace": 0x2A,
    "Space": 0x2C,
    "Enter": 0x28,
    "Tab": 0x2B,
    "Esc": 0x29,
    "Del": 0x4C,
    "Ins": 0x49,
    "Caps_Lock": 0x39,
    "Num_Lock": 144,
    "Mute": 0xef,

    "Home": 74,
    "End": 77,
    "PgUp": 75,
    "PgDown": 78,

    "Up": 0x52,
    "Down": 0x51,
    "Left": 0x50,
    "Right": 0x4F,

    "`": 0x35,
    "1": 0x1E,
    "!": [0x1E],
    "2": 0x1F,
    "@": [0x1F],
    "3": 0x20,
    "#": [0x20],
    "4": 0x21,
    "$": [0x21],
    "5": 0x22,
    "%": [0x22],
    "6": 0x23,
    "^": [0x23],
    "7": 0x24,
    "&": [0x24],
    "8": 0x25,
    "9": 0x26,
    "(": [0x26],
    "0": 0x27,
    ")": [0x27],

    "=": 0x2E,
    "+": 0x57,
    "-": 0x56,
    "*": 0x55,
    "/": 0x54,
    "|": [0x31],

    "'": 0x34,
    '"': [0x34],
    "?": [0x38],
    ",": 0x36,
    "<": [0x36],
    ".": 0x37,
    ">": [0x37],
    "\\": 0x64,
    "[": 0x2F,
    "{": [0x2F],
    "]": 0x30,
    "}": [0x30],
    ";": 0x33,
    ":": [0x33],

    "F1": 0x3A,
    "F2": 0x3B,
    "F3": 0x3C,
    "F4": 0x3D,
    "F5": 0x3E,
    "F6": 0x3F,
    "F7": 0x40,
    "F8": 0x41,
    "F9": 0x42,
    "F10": 0x43,
    "F11": 0x44,
    "F12": 0x45,
}
