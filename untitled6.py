from mcpi.minecraft import Minecraft 
mc=Minecraft.create()

while True:
    pos = mc.player.getTilePos()
    haha="(x,y,z)"
    mc.postToChat(haha+str(pos))
