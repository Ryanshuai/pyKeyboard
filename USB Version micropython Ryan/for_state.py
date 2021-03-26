# -*- coding: utf-8 -*-

import pyb
kb = pyb.USB_HID()

buf = bytearray(1)
while True:
    if kb.recv(buf, timeout=20) > 0:
        print(buf)