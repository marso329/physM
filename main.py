from loader.setup import *
from objects import cube
temp=cube.cube(2,1,1,"RED")
#temp.set_solid()
set_background_color("BLUE")
set_background_alpha(1.0)
glutMainLoop()