# -*- coding: utf-8 -*-

import pyb


class LinearIO:
    def __init__(self, io_names):
        self.ios = [pyb.Pin(io_name, pyb.Pin.IN, pyb.Pin.PULL_UP) for io_name in io_names]
        self.counters = [0] * len(io_names)

    def update(self):
        for idx, out_pin in enumerate(self.ios):
            value = out_pin.value()
            self.counters[idx] += 1 - 2 * value
            self.counters[idx] = max(min(self.counters[idx], 5), 0)

    def pushed(self):
        pushed_pos = list()
        for idx, count in enumerate(self.counters):
            if count == 5:
                pushed_pos.append(idx)
        return pushed_pos


class MatrixIO:
    def __init__(self, raw_io_names, column_io_names):
        self.raw_ios = [pyb.Pin(io_name, pyb.Pin.IN, pyb.Pin.PULL_UP) for io_name in raw_io_names]
        self.col_ios = [pyb.Pin(io_name, pyb.Pin.OUT_OD) for io_name in column_io_names]
        self.counters = [[0] * len(column_io_names) for i in range(len(raw_io_names))]

    def update(self):
        for col, out_pin in enumerate(self.col_ios):
            out_pin.low()
            for row, in_pin in enumerate(self.raw_ios):
                self.counters[row][col] += 1 - 2 * in_pin.value()
                self.counters[row][col] = max(min(self.counters[row][col], 5), 0)
            out_pin.high()

    def pushed(self):
        pushed_pos = list()
        for row, row_count in enumerate(self.counters):
            for col, col_count in enumerate(row_count):
                if col_count == 5:
                    pushed_pos.append((row, col))
        return pushed_pos
