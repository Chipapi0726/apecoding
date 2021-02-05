from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random,time
x,y,z=mc.player.getPos()
myID=mc.getPlayerEntityId("jjmega726")
mc.postToTitle(myID,'遊戲開始!請往金磚走')
mc.setBlocks(x+3,y-3,z+3,x-3,y-1,z-3,57)
mc.setBlocks(x+2,y-2,z+2,x-2,y-1,z-2,0)
mc.setBlocks(x,y-3,z+3,x,y-1,z+3,0)
mc.setBlock(x,y-3,z+3,41)
while True:
    x,y,z=mc.player.getPos()
    a=mc.getBlock(x,y-1,z)
    b=mc.getBlock(x,y-1,z)
    c=mc.getBlock(x,y-1,z)
    d=mc.getBlock(x,y-1,z)
    if a==41:
        x,y,z=mc.player.getPos()
        mc.postToTitle(myID,'踩在白色羊毛上')
        mc.setBlocks(x,y-1,z,x,y-1,z+9,57)
        mc.setBlock(x,y-1,z+10,35)
    if b==35:
        x,y,z=mc.player.getPos()
        mc.setBlocks(x+4,y-1,z+4,x-4,y-1,z-4,22)
        mc.setBlock(x,y-1,z,173)
        mc.postToTitle(myID,'射箭!讓我們吃雞吧!')
    if d==22:
        x,y,z=mc.player.getPos()
        mc.setBlocks(x+10,y-2,z+21,x-10,y-2,z+1,170)
        mc.setBlocks(x+10,y-1,z+21,x-10,y-1,z+1,188)
        mc.setBlocks(x+9,y-1,z+20,x-9,y-1,z+2,0)
        break
    
for i in range(11):
    position=mc.player.getPos()
    x=position.x+random.uniform(+9,-9)
    y=position.y+random.uniform(-1,-1)
    z=position.z+random.uniform(+20,2)
    mc.spawnEntity(x,y,z,93)

   

mc.postToTitle(myID,"20秒 遊戲")

time.sleep(20)

mc.postToTitle(myID,"遊戲結束")

        

        
        
        
        
        
        
        
        
        

        
          
    
    
    
   
      
            
       

    