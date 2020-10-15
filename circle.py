# Finish drawing traffic lights

WIDTH = 600
HEIGHT = 600

def draw():
    screen.clear()
    screen.draw.circle((250,250), 50, "white")
    screen.draw.filled_circle((250, 100), 50, "green")
    screen.draw.circle((250,400),50, "purple")
    screen.draw.circle((600,400),50, "purple")
    screen.draw.line((0,0), (600, 600), "orange")

