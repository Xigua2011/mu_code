import random

guesses=0
b=random.randint(0,50)
while(True):
    guesses = guesses + 1
    g = input('enter a guess')
    g = int(g)
    if b==g:
        print("correct")
        break
    elif g<b:
        print("guess lower")
    elif g>b:
        print("guess higher")
print("number of guesses you had", guesses)
