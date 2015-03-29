from loader.setup import *
from objects import cube, objectFile, sphere, cylinder,line
from elevator_simulator import elevator

main_elevator=elevator.elevator()
var.viewing_position=(15,15,15)
bind_key(con.UP, main_elevator.open_doors)
bind_key(con.DOWN, main_elevator.close_doors)
number_of_floors=5
for i in range(number_of_floors):
    floor1=cube.cube(30,10,1,"BLUE")
    floor1.change_position(21, 0, -7.5+i*16)
def update_camera_position():
    var.viewing_center=main_elevator.get_position()
    temp=main_elevator.get_position()
    temp=(temp[0]+15,temp[1]+15,temp[2]+15)
    var.viewing_position=temp
def change_elevator_direction():
    main_elevator.floor.position_change[2]*=-1
add_function_to_mainloop(update_camera_position)
bind_key(con.LEFT, change_elevator_direction)
glutMainLoop()