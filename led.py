from microbit import *

while True:
    pin2.write_analog(1023)
    sleep(500)
    pin2.write_analog(500)
    sleep(1000)

