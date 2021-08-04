import digitalio


def input_io(io):
    pin = digitalio.DigitalInOut(io)
    pin.switch_to_input(pull=digitalio.Pull.UP)
    return pin


def output_io(io):
    pin = digitalio.DigitalInOut(io)
    pin.switch_to_output(drive_mode=digitalio.DriveMode.OPEN_DRAIN)
    return pin


class LinearIO:
    def __init__(self, io_names):
        self.ios = [input_io(io_name) for io_name in io_names]

    def update(self):
        pushed_pos = set()
        for idx, out_pin in enumerate(self.ios):
            if out_pin.value == 0:
                pushed_pos.add(idx)
        return pushed_pos


class MatrixIO:
    def __init__(self, y_io_names, x_io_names):
        self.y_ios = [input_io(io_name) for io_name in y_io_names]
        self.x_ios = [output_io(io_name) for io_name in x_io_names]

    def update(self):
        pushed_pos = set()
        for j, out_pin in enumerate(self.x_ios):
            out_pin.value = 0
            for i, in_pin in enumerate(self.y_ios):
                if in_pin.value == 0:
                    pushed_pos.add((i, j))
            out_pin.value = 1
        return pushed_pos
