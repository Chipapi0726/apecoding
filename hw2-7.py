from mcpi.minecraft import Minecraft
mc=Minecraft.create()
a=input('who are you?')
mc.postToChat('Hello'+a+'lalalala')
x,y,z=mc.player.getPos()
mc.setBlocks(x,y,z,x+6,y+6,z+6,57)
mc.setBlocks(x+1,y+1,z+1,x+5,y+5,z+5,0)
mc.setBlocks(x,y+4,z,x+6,y+4,z+6,57)
mc.setBlocks(x,y+1,z+4,x,y+2,z+4,0)
