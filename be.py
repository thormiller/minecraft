# Base project format.
# Documentation https://github.com/raspberrypilearning/getting-started-with-minecraft-pi/blob/master/worksheet.md
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init():
    mc = Minecraft.create("127.0.0.1", 4711)
    mc.setting("world_immutable",True)
    #x, y, z = mc.player.getPos()        
    return mc

def woolTest(mc,x,y,z):
    m =[32]
    print("LIST m LENGTH =",len(m))
    for l in range (0,len(m)):
        print(m[l],"",end="")
        mc.setBlock(x,y,z+l,35,m[l])
 
 
def thor(mc,x,y,z):
    
    t = ["0000000000",
         "0000000000",
         "1111111111",
         "    1111  ",
         "    1111  ",
         "    1111  ",
         "    1111  ",
         "0000000000",
         "0000000000",
         "0000000000"]
    for k in range(0,10):
      for l in range(0,10):
             m = 0 
             theBlock = t[k][l]
             if (theBlock ==" "):
                 m = 0
             if (theBlock =="0"):
                 m = 3
             if (theBlock =="1"):
                 m = 4
             mc.setBlock(x,9+y,z,35,m)
             print(t)

def tho(mc,x,y,z):
    b = ["0000000000",
         "0000000000",
         "1111111111",
         " 1111 111 ",
         " 1111111  ",
         "    1111  ",
         "  1111    ",
         "0000000000",
         "0000000000",
         "0000000000"]
    for k in range(0,10):
      for l in range(0,10):
             m = 0 
             theBlock = b[k][l]
             if (theBlock ==" "):
                 m = 0
             if (theBlock =="0"):
                 m = 2
             if (theBlock =="1"):
                 m = 8
             mc.setBlock(1+x,40+y,z,35,m)
             print(m)
             
             
def colors(mc,x,y,z):
    done = 0
    thecolor = 0
    while(done< 32):
        mc.setBlock(x+10, y+10, z+done, 35, thecolor)
        done= done + 3
        thecolor = thecolor + 2
 
 
def main():
    mc =init()
    x,y,z = mc.player.getPos()
    thor(mc,x,y,z)
    tho(mc,x,y,z)
    colors(mc,x,y,z)
    mc.player.setPos(x,y,z+5)
    
if __name__ == "__main__":
    main()
