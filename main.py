from loader.setup import *
from objects import cube,objectFile

#temp=cube.cube(1,1,1,"RED")
#temp.set_solid()
#temp.change_position_change(0.0001,0.00001, 0)
#temp.change_rotation_change(0.01,0.01, 0)
#temp.set_transparency(0.1)


#temp1=cube.cube(1,1,1,"RED")
#temp1.change_position(1, 0, 0)
#temp1.change_position_change(-0.0001,-0.00001, 0)
#temp1.change_rotation_change(-0.01,-0.01, 0)
#temp.move_with(temp1)
#temp.rotate_with(temp1)
temp=objectFile.objectFile("teapot.obj")
temp.change_rotation_change(10, 10,0 )

set_background_color("BLUE")



def bind_function():
    change_viewing_position(0.1, 0, 0)
bind_key(con.UP,bind_function )

def bind_function1():
    change_viewing_position(-0.1, 0, 0)
bind_key(con.DOWN,bind_function1 )
glutMainLoop()