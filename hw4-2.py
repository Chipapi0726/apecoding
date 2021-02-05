from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random
x,y,z=mc.player.getPos()
mc.setBlock(x,y-1,z,57)
for i in range(20):
    r=random.choice(range(1,7))
    if r==1:
        mc.setBlocks(x+1,y-1,z,x+2,y-1,z,35,1)
        x=x+2
    if r==2:
        mc.setBlocks(x-1,y-1,z,x-2,y-1,z,35,2)
        x=x-2
    if r==3:
        mc.setBlocks(x,y-1,z+1,x,y-1,z+2,35,3)
        z=z+2
    if r==4:
        mc.setBlocks(x,y-1,z-1,x,y-1,z-2,35,4)
        z=z-2
    if r==5:
        mc.setBlocks(x,y-1,z,x,y-3,z,35,5)
        y=y-2
    if r==6:
        mc.setBlocks(x,y-1,z,x,y+1,z,35,6)
        y=y+2
        
