# Draw a backround image with Krita, save it as png file
# Draw an alien image, save it as png file
# Draw a girl image, save it as png file

import pygame

joystick = pygame.joystick.Joystick(0)
joystick.init()

WIDTH = 600
HEIGHT = 600

background = Actor("background")
alien = Actor("face")
alien.x = 200
alien.y = 200

def draw():
    screen.clear()
    background.draw()
    alien.draw()

def update():
    if keyboard.right or joystick.get_axis(0) > 0.5:
        alien.x = alien.x + 4
    if keyboard.left or joystick.get_axis(0) < -0.5:
        alien.x = alien.x - 4

    if alien.x > 600:
        alien.x = 0
    print(joystick.get_axis(0))
    if alien.x < -36:
        alien.x = 600
    if alien.y < -36:
        alien.y = 600
    if alien.y > 636:
        alien.y = 0

    if keyboard.down:
        alien.y = alien.y + 4
    if keyboard.up:
        alien.y = alien.y - 4

