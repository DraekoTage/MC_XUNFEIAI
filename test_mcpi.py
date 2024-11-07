from mcpi.minecraft import Minecraft
import mcpi.block as block
import time

if __name__ == '__main__':
    # 给点时间切换到mc窗口 方便观察
    time.sleep(3)
    
    # 连接到MC
    mc = Minecraft.create()
    
    # 得到角色当前的位置
    x, y, z = mc.player.getTilePos()
    conunt = 0
    for i in range(8):
        for j in range(8):
            for k in range(8):
                mc.setBlock(x+3+j, y+k, z+i, 35, i)
                mc.postToChat(conunt)
                conunt = conunt+1
            
                