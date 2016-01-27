from loader.setup import *
from objects import cube, objectFile, sphere, cylinder, line, light, textureCube
import random
import physMMath


def texture_cube():
    temp_cube = textureCube.textureCube(1, 1, 1, "NeHe.bmp")
    temp_cube.change_angular_velocity(20, 0, 0)
    temp_cube.change_velocity(-1, 0, 0)
    
    temp_cube1 = textureCube.textureCube(1, 1, 1, "NeHe.bmp")
    temp_cube1.change_position(-5, 0, 0)
    temp_cube1.change_velocity(3, 0, 0)
    
    var.viewing_position = (5, 5, 5)
    temp_light = light.light(0, 0, 5)
    bind_key(con.UP, temp_light.turn_light_on)
    bind_key(con.DOWN, temp_light.turn_light_off)
    glutMainLoop()
    
def test_move():
    temp_cube = cube.cube(1, 1, 1, "RED")
    # temp_cube.move_to(5, 5, 5, 1)
    # temp_cube.move_to(0, 0, 0, 1)
    temp_cube.move_to(0, 0, 5, 1)
    temp_cube.set_solid()
    var.viewing_position = (10, 10, 5)
    glutMainLoop()
def rotating_cube():
    temp_cube = cube.cube(1, 1, 1, "RED")
    temp_cube.set_solid()
    temp_cube.change_position(0, 0, 0)
    temp_cube.change_angular_velocity(-10, 0, 0)
    var.viewing_position = (5, 5, 5)
    var.light_position = (0, 0, 5, 1)
    glutMainLoop()
    
def ligtning_test():
    temp_light = light.light(0, 0, 5)
    def increase_ambient():
        temp_light.ambient[0]+=0.1
        glLightfv(temp_light.light, GL_AMBIENT, temp_light.ambient)
    def decrease_ambient():
        temp_light.ambient[0]-=0.1
        glLightfv(temp_light.light, GL_AMBIENT, temp_light.ambient)
    
    #temp_light = light.light(0, 0, 5)
    # temp_light=light.light(-5,0,5)
    temp_sphere = sphere.sphere(1, "RED")
    
    temp_cube = cube.cube(1, 1, 1, "BLUE")
    temp_cube.set_solid()
    temp_cube.change_position(2, 0, 0)
    temp_cube.change_velocity(-1, 0, 0)
    temp_cube.change_angular_velocity(200, 0, 0)
    bind_key(con.LEFT, increase_ambient)
    bind_key(con.RIGHT, decrease_ambient)
    bind_key(con.UP, temp_light.turn_light_on)
    bind_key(con.DOWN, temp_light.turn_light_off)
    var.viewing_position = (5, 5, 5)
    var.light_position = (0, 0, 6, 1)
    glutMainLoop()

def test_collision_high_speed():
    # first sphere with normal
    temp_sphere = sphere.sphere(1, "BLUE")
    temp_sphere.change_position(3, 0, 0)
    temp_sphere.change_velocity(-5, 0, 0)
    
    # first cube with normal
    temp_cube = cube.cube(1, 1, 1, "RED")
    temp_cube.set_solid()
    temp_cube.change_position(-3, 0, -1)
    temp_cube.change_velocity(1, 0, 0)
    
    # second cube without normal
    temp_cube1 = cube.cube(1, 1, 1, "GREEN")
    temp_cube1.set_solid()
    temp_cube1.change_position(0, 3, -1)
    temp_cube1.change_velocity(0, -5, 0)
    
    # normals
    temp_line = line.line((0, 0, 0), (1, 1, 1), "MAGENTA")
    temp_line2 = line.line((0, 0, 0), (1, 1, 1), "GREEN")
    
    def update():
        temp = temp_sphere.get_boundary_point(temp_cube)
        temp = temp_sphere.get_normal(temp)
        temp_normal = temp
        temp_normal = (temp_normal[0] * 8, temp_normal[1] * 8, temp_normal[2] * 8)
        temp = (temp[0] * 4, temp[1] * 4, temp[2] * 4)
        temp_line.points = (temp_sphere.position, (temp_sphere.position[0] + temp_normal[0], temp_sphere.position[1] + temp_normal[1], temp_sphere.position[2] + temp_normal[2]))
        temp1 = temp_cube.get_boundary_point(temp_sphere)
        temp1 = temp_cube.get_normal(temp1)
        temp1 = (temp1[0] * 8, temp1[1] * 8, temp1[2] * 8)
        temp1 = (temp_cube.position[0] + temp1[0], temp_cube.position[1] + temp1[1], temp_cube.position[2] + temp1[2])
        temp_line2.points = (temp_cube.position, temp1)
    add_function_to_mainloop(update)
    glutMainLoop()
def test_teapot(file="teapot.obj"):
    teapot=objectFile.objectFile(file)
    teapot.set_color("RED")
    teapot.change_angular_velocity(50, 0, 0)
    temp_light = light.light(0, 0, 5)
    
    temp_cube = cube.cube(2, 2, 1, "BLUE")
    temp_cube.set_solid()
    temp_cube.change_position(0, 0, -1)
    
    var.viewing_position = (0.6499999999999929, -0.5, 1.4100000000000006)
    def up():
        var.viewing_position =  (var.viewing_position[0]+0.1,var.viewing_position[1],var.viewing_position[2])
        
    def down():
        var.viewing_position =  (var.viewing_position[0]-0.11,var.viewing_position[1],var.viewing_position[2])
    def left():
        var.viewing_position =  (var.viewing_position[0],var.viewing_position[1]+0.1,var.viewing_position[2])
        
    def right():
        var.viewing_position =  (var.viewing_position[0],var.viewing_position[1]-0.1,var.viewing_position[2])
    
    def z_down():
        var.viewing_position =  (var.viewing_position[0],var.viewing_position[1],var.viewing_position[2]-0.11)
        
    def z_up():
        var.viewing_position =  (var.viewing_position[0],var.viewing_position[1],var.viewing_position[2]+0.1)
        print(var.viewing_position)
    
    
    bind_key(con.DOWN, down)
    bind_key(con.UP, up)
    bind_key(con.LEFT, left)
    bind_key(con.RIGHT, right)
    bind_key(con.PAGE_UP, z_up)
    bind_key(con.PAGE_DOWN, z_down)
    glutMainLoop()
def test_bunny():
    test_teapot("bunny.obj")
#test_bunny()       
texture_cube()
#ligtning_test()