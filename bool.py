print("Is it sunny today? Enter Y or N")
a = input()
if a == "Y" or a == "y":
    sunny = True
else:
    sunny = False

print("Is it windy today? Enter Y or N")
a = input()
if a == "Y" or a == "y":
    windy = True
else:
    windy = False

if sunny and not windy:
    print("You can go to the park")
elif sunny and windy:
    print("You can go to the park and fly your kite")
else:
    print("You must stay at home")
