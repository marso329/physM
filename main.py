from loader.setup import *
from objects import cube, objectFile, sphere, cylinder,line
import random
import physMMath


temp_sphere=sphere.sphere(1,"BLUE")
temp_sphere.change_position(3, 0, 0)
temp_sphere.change_velocity(-5, 0,0)
print(temp_sphere.max_distance_from_centre)

temp_cube=cube.cube(1,1,1,"RED")
temp_cube.set_solid()
temp_cube.change_position(-3, 0, -1)
temp_cube.change_velocity(1, 0, 0)

temp_cube1=cube.cube(1,1,1,"GREEN")
temp_cube1.set_solid()
temp_cube1.change_position(0, 3, -1)
temp_cube1.change_velocity(0, -5, 0)

#new_sphere1=sphere.sphere(0.1,"YELLOW")
##new_sphere1.collision_enabled=False
#new_sphere2=sphere.sphere(0.1,"MAGENTA")
#new_sphere2.collision_enabled=False
enable_fps_counter()
temp_line=line.line((0,0,0),(1,1,1),"MAGENTA")

temp_line2=line.line((0,0,0),(1,1,1),"GREEN")
def print_function():
    temp=temp_sphere.get_boundary_point(temp_cube)
    temp=temp_sphere.get_normal(temp)
    temp_normal=temp
    temp_normal=(temp_normal[0]*8,temp_normal[1]*8,temp_normal[2]*8)
    temp=(temp[0]*4,temp[1]*4,temp[2]*4)
    #new_sphere2.position=list(temp_sphere.get_boundary_point(temp_cube))
    temp_line.points=(temp_sphere.position,(temp_sphere.position[0]+temp_normal[0],temp_sphere.position[1]+temp_normal[1],temp_sphere.position[2]+temp_normal[2]))
    
    temp1=temp_cube.get_boundary_point(temp_sphere)
    temp1=temp_cube.get_normal(temp1)
    temp1=(temp1[0]*8,temp1[1]*8,temp1[2]*8)
    temp1=(temp_cube.position[0]+temp1[0],temp_cube.position[1]+temp1[1],temp_cube.position[2]+temp1[2])
    temp_line2.points=(temp_cube.position,temp1)
    
   # new_sphere1.position=list(temp_cube.get_boundary_point(temp_sphere))
def while_func():
    while True:
        pass
bind_key(con.UP, while_func)
    #print(var.current_fps)
add_function_to_mainloop(print_function)
glutMainLoop()
