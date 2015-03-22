from loader.setup import *
from objects import cube, objectFile, sphere, cylinder

# a testcube which is a floor
temp1 = cube.cube(20, 20, 2, "RED")
temp1.set_solid()
temp1.change_position(0, -5, 0)
temp1.change_angular_displacement(0, 0, 0)

# a testcube 
temp_cube = cube.cube(5, 5, 5, "RED")
temp_cube.set_solid()
temp_cube.change_position(0, -5, 15)
temp_cube.enable_gravity()


# a testsphere
temp2 = sphere.sphere(5.0, "YELLOW")
temp2.change_position(0, 0, 10)
temp2.change_velocity(0, 0, 2)
temp2.enable_gravity()

# a testcylinder
test_cylinder = cylinder.cylinder(1, 5, "MAGENTA")
test_cylinder.change_angular_velocity(0, 10, 10)
test_cylinder.enable_gravity()


# a test .obj file
temp = objectFile.objectFile("teapot.obj")
temp.change_angular_velocity(10, 10, 0)
temp.set_transparency(0.2)
temp.enable_gravity()

# some enviromentsetups
set_background_color("BLUE")
enable_fps_counter()
hold_fps(30)

def fps_func():
    # print(var.current_fps)
    print(temp_cube.get_boundary_point(temp1))
add_function_to_mainloop(fps_func)
def bind_function():
    change_viewing_position(0.1, 0, 0)
bind_key(con.UP, bind_function)

def bind_function1():
    change_viewing_position(-0.1, 0, 0)
def bind_function2():
    change_viewing_position(0, 1.0, 0)
def bind_function3():
    change_viewing_position(0, -1.0, 0)
bind_key(con.DOWN, bind_function1)
bind_key(con.LEFT, bind_function2)
bind_key(con.RIGHT, bind_function3)
glutMainLoop()
