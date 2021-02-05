from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getPos()
for i in range(50):
    x,y,z=mc.player.getPos()
    x=x+i
    mc.setBlock(x,y-1,z,57)
mc.player.setBlocks(x,y,z,x+6,y+6,z+6,57)
mc.player.setBlocks(x+1,y+1,z+1,x+5,y+5,z+5,0)