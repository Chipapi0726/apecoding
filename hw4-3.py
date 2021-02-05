from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random
x,y,z=mc.player.getPos()



for i in range(100):
    x+=1
    for j in range(10):
        color=random.randrange(0,16)
        mc.setBlock(x,y,z,35,color)
        z+=1
    z-=10