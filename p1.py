# Write your code here :-)
from richlib import *

WIDTH = 1000
HEIGHT = 1000

cube1 = Cube((50, 0, 0))
cube2 = Cube((-50, 30, 10))
sphere = Sphere((0, 0, 50))

cube1.color = (150, 0, 0)
cube2.color = GREEN


def draw():
    clear()
    cube1.draw()
    cube2.draw()
    sphere.draw()


run()
