from microbit import *
boat = Image("90090:"
             "99099:"
             "00900:"
             "99099:"
             "09990:")
while True:
    gesture = accelerometer.current_gesture()
    #Why do we need this gesture line?
    if button_a.is_pressed():
        display.show(boat)
    elif button_b.is_pressed():
        display.scroll("Animals are cute")
    else:
        display.clear()

