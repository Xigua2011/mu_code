print("How old are you?")
age = int(input())
print("How tall are you?")
height = int(input())
print("What is the temperature?")
temp = int(input())
if (age >= 12 or height >= 140) and (temp <= 30) and (temp >= 10 ):
    print("you can ride the rollercoaster")
else:
    print("YOU MAY NOT RIDE, GO AWAY!")
