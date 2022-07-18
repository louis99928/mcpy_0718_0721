from mcpi.minecraft import Minecraft
mc=Minecraft.create()
pos = mc.player.getTilePos()
mc.player.setTilePos(pos.x+100,pos.y,pos.z)
print(pos)