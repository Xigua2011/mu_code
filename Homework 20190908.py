# Draw a backround image with Krita, save it as png file
# Draw an badguy image, save it as png file
# Draw a girl image, save it as png file
# Make score increase when badguy colliderect

WIDTH = 600
HEIGHT = 600

background = Actor("background")
alien = Actor("dog")
alien.x = 200
alien.y = 200
score = 0

badguy = Actor("polarbear")
person = Actor("penguin")

safe = False

def draw():
    screen.clear()
    background.draw()
    alien.draw()
    badguy.draw()
    person.draw()
    score_string = str(score)
    screen.draw.text("score: "+score_string, (0,0), color='red')

    if safe:
        screen.draw.text("you are safe",(100,0),color='pink')
    else:
        screen.draw.text("you are not safe",(100,0),color='purple')


def update():
    global score, safe
    if keyboard.right:
        alien.x = alien.x + 6
    if keyboard.left:
        alien.x = alien.x - 6
    if keyboard.down:
        alien.y = alien.y + 6
    if keyboard.up:
        alien.y = alien.y - 6

    if keyboard.d:
        badguy.x = badguy.x + 6
    if keyboard.a:
        badguy.x = badguy.x - 6
    if keyboard.s:
        badguy.y = badguy.y + 6
    if keyboard.w:
        badguy.y = badguy.y - 6

    if alien.x > 600:
        alien.x = 0
    if alien.x < -36:
        alien.x = 600
    if alien.y < -36:
        alien.y = 600
    if alien.y > 636:
        alien.y = 0

    if alien.x > 134 and alien.x < 302 and alien.y > 110 and alien.y < 266:
        safe = True
    else:
        safe = False
    print(alien.x, alien.y, safe)

    if badguy.x > 600:
        badguy.x = 0
    if badguy.x < -36:
        badguy.x = 600
    if badguy.y < -36:
        badguy.y = 600
    if badguy.y > 636:
        badguy.y = 0

    if badguy.colliderect(alien) and not safe:
        sounds.eep.play()
        score += 1

