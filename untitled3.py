

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

for i in range(50):
    x,y,z=mc.player.getPos()
    x=x+i
    mc.setBlock(x,y-1,z,41)
mc.setBlocks(x,y-1,z,x+6,y+6,z+6,41)
mc.setBlocks(x+1,y,z+1,x+5,y+5,z+5,0)