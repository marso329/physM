from loader.setup import *
from objects import cube, objectFile, sphere, cylinder
import random
import physMMath

temp_cube=cube.cube(1,1,1,"RED")
temp_cube.set_solid()
temp_cube.change_position(0, 0, 2)
temp_cube.change_velocity(0, -1, 0)


temp_cube1=cube.cube(1,1,1,"BLUE")
temp_cube1.set_solid()
temp_cube1.change_position(0, 0, -2)
temp_cube1.change_velocity(0, 0, 0)
temp_cube.change_angular_velocity(30, 0, 0)
enable_fps_counter()
def print_function():
    position=temp_cube.get_boundary_point(temp_cube1)
    #print(position)
    print(var.current_fps)
add_function_to_mainloop(print_function)

glutMainLoop()
