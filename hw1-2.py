from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

while True:
    mc.postToChat('YO WHATS UP')
    time.sleep(0.5)
