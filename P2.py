from richlib import *

cube = Actor('trooper')
cube.size=(20,20,20)
#Cube((0, 10, 0), (10, 40,10), 'blue')

def draw():
    clear()
    cube.draw()


def update():
    cube.x = cube.x + 4
    if cube.x > 100:
        cube.x = -100


run()
