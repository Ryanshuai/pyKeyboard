import pyb

hid = pyb.USB_HID()


def decode_keys(state_keys, mat_keys):
    byte0 = 0
    if "ctrl" in state_keys:
        byte0 |= 1
    if "shift" in state_keys:
        byte0 |= 2
    if "alt" in state_keys:
        byte0 |= 4
    if "win" in state_keys:
        byte0 |= 8

    key_hex_codes = set()
    for key in mat_keys:
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

    "back": 0x2A,
    "space": 0x2C,
    "enter": 0x28,
    "tab": 0x2B,
    "esc": 0x29,
    "delete": 0x4C,

    "up": 0x52,
    "down": 0x51,
    "left": 0x50,
    "right": 0x4F,

    "0": 0x27,
    "1": 0x1E,
    "2": 0x1F,
    "3": 0x20,
    "4": 0x21,
    "5": 0x22,
    "6": 0x23,
    "7": 0x24,
    "8": 0x25,
    "9": 0x26,
    "=": 0x2E,
    "+": 0x57,
    "-": 0x56,
    "*": 0x55,
    "/": 0x54,
    "%": 0x22,
    "&": 0x24,
    "|": 0x31,
    "!": 0x1E,
    "^": 0x23,

    "'": 0x34,
    "<": [0x36],
    ">": [0x37],
    "#": 0x20,
    "@": 0x1F,
    "?": 0x38,
    "(": [0x26],
    ")": [0x27],
    ".": 0x37,
    ",": 0x36,
    "\\": 0x64,
    "[": 0x2F,
    "]": 0x30,
    ":": [0x33],
    ";": 0x33,
    "$": 0x21,
    "{": [0x2F],
    "}": [0x30],
    '"': [0x34],

    "f1": 0x3A,
    "f2": 0x3B,
    "f3": 0x3C,
    "f4": 0x3D,
    "f5": 0x3E,
    "f6": 0x3F,
    "f7": 0x40,
    "f8": 0x41,
    "f9": 0x42,
    "f10": 0x43,
    "f11": 0x44,
    "f12": 0x45,
}
