import storage, usb_cdc
import board, digitalio

# In this example, the button is wired to connect D2 to +V when pushed.
button = digitalio.DigitalInOut(board.GP12)
button.switch_to_input(pull=digitalio.Pull.UP)

# Disable devices only if button is not pressed.
if button.value:
    storage.disable_usb_drive()
    usb_cdc.disable()
