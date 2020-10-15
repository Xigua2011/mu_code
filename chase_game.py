import random
WIDTH = 600
HEIGHT = 600

background = Actor("background")
dog = Actor("dog")
dog.x = 200
dog.y = 200
score = 0
score2 = 0

polarbear = Actor("polarbear")
penguin = Actor("penguin")

safe = False

def draw():
    screen.clear()
    background.draw()
    dog.draw()
    polarbear.draw()
    penguin.draw()
    score_string = str(score)
    screen.draw.text("score: "+score_string, (0,0), color='red')
    score2_string = str(score2)
    screen.draw.text("score2: "+score2_string, (200,0), color='green')
    BOX = Rect((200, 200), (100, 100))
    if score >= 10 or score2 >= 10:
        screen.draw.filled_rect(BOX, 'purple')
        screen.draw.textbox("you have won the game!",BOX, color='blue')


def update():
    global score, safe, score2
    if keyboard.right:
        dog.x = dog.x + 6
    if keyboard.left:
        dog.x = dog.x - 6
    if keyboard.down:
        dog.y = dog.y + 6
    if keyboard.up:
        dog.y = dog.y - 6

    if keyboard.d:
        polarbear.x = polarbear.x + 6
    if keyboard.a:
        polarbear.x = polarbear.x - 6
    if keyboard.s:
        polarbear.y = polarbear.y + 6
    if keyboard.w:
        polarbear.y = polarbear.y - 6

    if dog.x > 600:
        dog.x = 0
    if dog.x < -36:
        dog.x = 600
    if dog.y < -36:
        dog.y = 600
    if dog.y > 636:
        dog.y = 0

    if dog.x > 134 and dog.x < 302 and dog.y > 110 and dog.y < 266:
        safe = True
    else:
        safe = False
    print(dog.x, dog.y, safe)

    if polarbear.x > 600:
        polarbear.x = 0
    if polarbear.x < -36:
        polarbear.x = 600
    if polarbear.y < -36:
        polarbear.y = 600
    if polarbear.y > 636:
        polarbear.y = 0

    if polarbear.colliderect(penguin):
        sounds.roaring.play()
        score += 1
        penguin.x = random.randint(0,600)
        penguin.y = random.randint(0,600)

    if dog.colliderect(penguin):
        sounds.barking.play()
        score2 += 1
        penguin.x = random.randint(0,600)
        penguin.y = random.randint(0,600)

#    if polarbear.colliderect(dog) and not safe:
#        sounds.eep.play()
#        score += 1

