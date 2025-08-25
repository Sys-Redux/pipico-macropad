import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time

# Create keyboard object
kbd = Keyboard(usb_hid.devices)

# Button pins
button_pins = [board.GP0, board.GP1, board.GP2, \
               board.GP3, board.GP4, board.GP5]
buttons = []
for pin in button_pins:
    btn = digitalio.DigitalInOut(pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP
    buttons.append(btn)

# LED pins
led_pins = [board.GP6, board.GP7, board.GP8]
leds = []
for pin in led_pins:
    led = digitalio.DigitalInOut(pin)
    led.direction = digitalio.Direction.OUTPUT
    leds.append(led)

while True:
    for i, button in enumerate(buttons):
        if not button.value:   # Button pressed
            leds[i % len(leds)].value = True
            # Send ctrl+alt+(Number) based on button
            kbd.send(Keycode.CONTROL, Keycode.ALT, \
                     getattr(Keycode, f"ONE") + i)
            time.sleep(0.2)
            leds[i % lens(leds)].value = False