from mcpi.minecraft import *
import time
mc = Minecraft.create()
mc.postToChat("Hello Minecraft World")
while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    print(pos)
    mc.postToChat(pos)
