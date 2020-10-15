from phue import Bridge
from rgbxy import Converter
from rgbxy import GamutA, GamutB, GamutC
from time import sleep
c = Converter(GamutA)
b = Bridge('192.168.0.2')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

anni = b.lights[0]
richard = b.lights[1]

def colour(c):
    anni.xy = c
    richard.xy = c

red = c.hex_to_xy('ff0000')
purple = c.hex_to_xy('8f42ff')
blue = c.hex_to_xy('45c7ff')
pink = c.hex_to_xy('ff73ff')
green = c.hex_to_xy('71ff42')

for i in range(100):
    colour(red)
    sleep(2)
    colour(green)
    sleep(2)
    colour(blue)
    sleep(2)


