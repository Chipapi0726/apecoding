from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

Position=mc.player.getTilePos()
x=Position.x
y=Position.y
z=Position.z
time.sleep(15)
mc.player.setTilePos(x,y,z)
