from mcpi.minecraft import Minecraft
import random
mc=Minecraft.create()
Block=random.randrange(0,150)
x,y,z=mc.player.getTilePos()
mc.setBlocks(x+10,y+10,z+10,x-10,y-10,z-10,0)