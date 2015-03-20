from loader.setup import *
from objects import cube,objectFile,sphere,cylinder

temp1=cube.cube(20,1,20,"RED")
temp1.set_solid()
temp1.change_position(0, -5, 0)

temp2=sphere.sphere(5.0,"YELLOW")
temp2.change_position(0, 0, 10)
temp2.change_position_change(0, 0, -0.001)
test_cylinder=cylinder.cylinder(1,5,"MAGENTA")
test_cylinder.change_rotation_change(0, 1, 1)
#temp1.change_position_change(0.0001,0.00001, 0)
#temp1.change_rotation_change(-0.01,0.00, 0)
#temp1.set_transparency(0.5)

#temp1=cube_displaylist.cube(1,1,1,"RED")
#temp1.set_solid()
#temp1.change_position_change(-0.0001,0, 0)
#temp1.change_rotation_change(0.01,0.01, 0)
#temp1.set_transparency(0.5)


#temp1=cube.cube(1,1,1,"RED")
#temp1.change_position(1, 0, 0)
#temp1.change_position_change(-0.0001,-0.00001, 0)
#temp1.change_rotation_change(-0.01,-0.01, 0)
#temp.move_with(temp1)
#temp.rotate_with(temp1)
temp=objectFile.objectFile("teapot.obj")
temp.change_rotation_change(0.1, 0.1,0 )
temp.set_transparency(0.2)

set_background_color("BLUE")
enable_fps_counter()
hold_fps(30)


def bind_function():
    change_viewing_position(0.1, 0, 0)
bind_key(con.UP,bind_function )

def bind_function1():
    change_viewing_position(-0.1, 0, 0)
def bind_function2():
    change_viewing_position(0, 1.0, 0)
def bind_function3():
    change_viewing_position(0, -1.0, 0)
bind_key(con.DOWN,bind_function1 )
bind_key(con.LEFT,bind_function2 )
bind_key(con.RIGHT,bind_function3 )
glutMainLoop()