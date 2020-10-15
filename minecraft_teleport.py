from mcpi.minecraft import *
import time
mc = Minecraft.create()

# CHANGE THESE NUMBERS TO THE CO-ORDS OF YOUR TELEPORTERS

teleporter_x = -15
teleporter_z = -1263

destination_x = 0
destination_y = 100
destination_z = -1256

height = 100

while True:

    pos = mc.player.getTilePos()

    if pos.x == teleporter_x and pos.z == teleporter_z:

        mc.postToChat("teleport!")
        # move off the teleporter tile so we dont land on it again
        pos.x += 1
        for i in range(0, height):
            pos.y = pos.y + 1  # move up a bit
            time.sleep(0.01) # short delay of 0.2 seconds
            mc.player.setTilePos(pos)


