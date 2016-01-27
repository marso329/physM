from loader.setup import *
from objects import cube, objectFile, sphere, cylinder,line
import random
import physMMath
import tests
from PIL.ImageChops import add

#tests.test_collision_high_speed()
#tests.rotating_cube()

#tests.ligtning_test()

#tests.test_move()
#tests.texture_cube()

temp_sphere1=sphere.sphere(1,"RED")
temp_sphere1.change_position(0, 0, 2)
temp_sphere1.change_velocity(0, 0, -2)
#temp_sphere1.enable_gravity()

temp_cube1=cube.cube(2,2,1,"BLUE")
temp_cube1.set_solid()
temp_cube1.affected_by_gravity=False
temp_cube1.change_position(0, 0, -5)
temp_cube1.change_velocity(0, 0, 1)
var.viewing_position=(10,10,10)
def print_function():
    print(temp_cube1.position_change)
add_function_to_mainloop(print_function)
glutMainLoop()