# -*- coding: utf-8 -*-

import machine
import pyb


col1 = pyb.Pin('A10', pyb.Pin.IN, pyb.Pin.PULL_UP)
pyb.delay(1000)

if col1.value():  # not pushed
    pyb.usb_mode('VCP+HID', hid=pyb.hid_keyboard)
    pyb.main('main.py')
else:
    pyb.usb_mode('VCP+MSC')
    pyb.main('keyboard_send.py')
