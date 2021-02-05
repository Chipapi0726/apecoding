from mcpi.minecraft import Minecraft
mc=Minecraft.create()
from random import randrange
answer=randrange(0,16)
myID=mc.getPlayerEntityId("jjmega726")

while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
       hit=hits[0]
       
       block=mc.getBlockWithData(hit.pos)
       data=block.data
       
       if data>answer:
           mc.postToChat('NOOOOOOO')
       elif data<answer:
           mc.postToChat('NOOOOOOO')
       else:
           mc.setBlock(hit.pos,57)
           mc.postToTitle(myID,'雪莉啊!')
           break
    

    
