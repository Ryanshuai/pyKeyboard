import board
import digitalio


def input_io(io):
    pin = digitalio.DigitalInOut(io)
    pin.switch_to_input(pull=digitalio.Pull.UP)
    return pin


def output_io(io):
    pin = digitalio.DigitalInOut(io)
    pin.switch_to_output(DriveMode=digitalio.DriveMode.OPEN_DRAIN)
    return pin


class LinearIO:
    def __init__(self, io_names):
        self.ios = [input_io(io_name) for io_name in io_names]
        self.last_pushed_pos = set()

    def update(self):
        pushed_pos = set()
        for idx, out_pin in enumerate(self.ios):
            if out_pin.value:
                pushed_pos.add(idx)

        added_pos = pushed_pos - self.last_pushed_pos
        removed_pos = self.last_pushed_pos - pushed_pos
        self.last_pushed_pos = pushed_pos
        return added_pos, removed_pos


class MatrixIO:
    def __init__(self, y_io_names, x_io_names):
        self.y_ios = [input_io(io_name) for io_name in y_io_names]
        self.x_ios = [output_io(io_name) for io_name in x_io_names]
        self.last_pushed_pos = set()

    def update(self):
        pushed_pos = set()
        for j, out_pin in enumerate(self.x_ios):
            out_pin.low()
            for i, in_pin in enumerate(self.y_ios):
                if in_pin.value:
                    pushed_pos.add((i, j))
            out_pin.high()

        added_pos = pushed_pos - self.last_pushed_pos
        removed_pos = self.last_pushed_pos - pushed_pos
        self.last_pushed_pos = pushed_pos
        return added_pos, removed_pos
