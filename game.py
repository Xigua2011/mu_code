# Draw a backround image with Krita, save it as png file
# Draw an alien image, save it as png file
# Draw a girl image, save it as png file

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
    alien.x = alien.x + 10
    if alien.x > 600:
        alien.x = 0
    print(keyboard.right)
