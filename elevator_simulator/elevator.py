from objects import cube, objectFile, sphere, cylinder,line

class elevator():
    def __init__(self):
        self.length = 10
        self.width = 10
        self.height = 15
        self.color="GRAY"
        self.open=False
        
        
        self.floor=cube.cube(self.length,self.width,1,self.color)
        self.floor.change_position(0, 0, -7.5)
        self.floor.collision_enabled=False
        self.floor.change_velocity(0, 0, 2)
        
        self.roof=cube.cube(self.length,self.width,1,self.color)
        self.roof.change_position(0, 0, 7.5)
        self.roof.collision_enabled=False
        self.roof.move_with(self.floor)
        
        self.left_side=cube.cube(self.length,1,self.height-1,self.color)
        self.left_side.change_position(0, -4.5, 0)
        self.left_side.collision_enabled=False
        self.left_side.move_with(self.floor)
        
        self.right_side=cube.cube(self.length,1,self.height-1,self.color)
        self.right_side.change_position(0, 4.5, 0)
        self.right_side.collision_enabled=False
        self.right_side.move_with(self.floor)
        
        self.left_door=cube.cube(1,self.length/2,self.height,self.color)
        self.left_door.change_position(6, -2.5, 0)
        self.left_door.collision_enabled=False
        self.left_door.move_with(self.floor)
        
        self.right_door=cube.cube(1,self.length/2,self.height,self.color)
        self.right_door.change_position(6, 2.5, 0)
        self.right_door.collision_enabled=False
        self.right_door.move_with(self.floor)
        
    def get_position(self):
        temp=self.floor.position
        return(temp[0],temp[1],temp[2]+7.5)
    def open_doors(self):
        if not self.open:
            self.left_door.move_relative(0, -5, 0, 2)
            self.right_door.move_relative(0, 5, 0, 2)
            self.open=True
    def close_doors(self):
        if self.open:
            self.left_door.move_relative(0, 5, 0, 2)
            self.right_door.move_relative(0, -5, 0, 2)
            self.open=False
        
        