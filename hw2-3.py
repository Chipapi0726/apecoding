.np.array([nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn1])
from mcpi.minecraft import Minecraft
import random,time
mc=Minecraft.create()
x,y,z=mc.player.getPos()
y-=1

while True:
    color=random.randrange(0,16)
    mc.setBlocks(x-10,y,z-10,x+10,y,z+10,95,color)
    time.sleep(0.5)