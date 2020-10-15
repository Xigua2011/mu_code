got_key = False

def room1():
    print("You are in a hallway. Exits are north and south.")
    i=input("Command?")
    if(i=="north"):
        room2()
    elif(i=="south"):
        if(got_key):
            print("you unlock the door")
            room3()
        else:
            print("the door is locked")
            room1()
    else:
        room1()


def room2():
    global got_key
    print("You are in a swimming pool. Exits are south.")
    i=input("Command?")
    if(i=="south"):
        room1()
    elif(i=="swim"):
        print("You swim to the bottom of the pool and find a long thin key")
        got_key = True
        room2()
    else:
        room2()

def room3():
    print("the end")
    sys.exit()
room1()
