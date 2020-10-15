print("How old are you?")
age = int(input())
print("How tall are you?")
height = int(input())
if age > 12 or (height > 140 and height < 180):
    print("you can ride the rollercoaster")
else:
    print("YOU MAY NOT RIDE, GO AWAY!")
