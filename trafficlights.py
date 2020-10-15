from microbit import *

while True:
    pin0.write_digital(1)
    if button_a.is_pressed():
        pin1.write_digital(1)
        pin0.write_digital(0)
        sleep(2000)
        pin2.write_digital(1)
        pin1.write_digital(0)
        sleep(1000)
        pin2.write_digital(0)

