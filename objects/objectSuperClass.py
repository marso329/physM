from OpenGL.GL import *
from OpenGL.GLU import *
import constants.constants as con
import variables.variables as var
import inspect
class objectSuperClass:
    def __init__(self):
        self.color=(1.0,1.0,1.0)
        self.solid=False
        self.angles=[0,0,0]
        self.position=[0,0,0]
        self.angles_change=[0,0,0]
        self.position_change=[0,0,0]
        self.transparency_enabled=False
        self.transparency=1.0
        self.move_with_object=False
        self.mover=None
        self.rotate_with_object=False
        self.rotater=None
        self.add_to_world()
    def set_transparency(self,trans):
        assert(isinstance(trans, (float,int)) and trans<=1.0 and trans>=0)
        self.transparency=trans
        self.transparency_enabled=True
    def load(self):
        caller = inspect.getouterframes(inspect.currentframe())[1][3]
        raise NotImplementedError(caller + ' must be implemented in subclass')
    def create(self):
        caller = inspect.getouterframes(inspect.currentframe())[1][3]
        raise NotImplementedError(caller + ' must be implemented in subclass')
    def update_angels(self):
        if not self.rotate_with_object:
            self.angles[0]+=self.angles_change[0]
            self.angles[1]+=self.angles_change[1]
            self.angles[2]+=self.angles_change[2]
        else:
            self.angles[0]+=self.angles_change[0]+self.rotater.angles_change[0]
            self.angles[1]+=self.angles_change[1]+self.rotater.angles_change[1]
            self.angles[2]+=self.angles_change[2]+self.rotater.angles_change[2]
    def update_position(self):
        if not self.move_with_object:
            self.position[0]+=self.position_change[0]
            self.position[1]+=self.position_change[1]
            self.position[2]+=self.position_change[2]
        else:
            self.position[0]+=self.position_change[0]+self.mover.position_change[0]
            self.position[1]+=self.position_change[1]+self.mover.position_change[1]
            self.position[2]+=self.position_change[2]+self.mover.position_change[2]
    def rotate(self):
        glRotatef(self.angles[0], 1.0, 0.0, 0.0)
        glRotatef(self.angles[1], 0.0, 1.0, 0.0)
        glRotatef(self.angles[2], 0.0, 0.0, 1.0)
    def move(self):
        glTranslatef(self.position[0], self.position[1], self.position[2])
    def update_everything(self):
        self.update_angels()
        self.update_position()
        self.move()
        self.rotate()
    def check_color(self,color):
        try:
            self.color=con.COLORS[color]
        except KeyError:
            self.color=con.STANDARD_COLOR
    def set_color(self,color):
        self.check_color(color)
    def check_if_float_or_int(self,value):
        return isinstance(value,(int, long,float))
    def set_solid(self):
        self.solid=True
    #adds itself to the world
    def add_to_world(self):
        var.objects_in_world[var.number_of_objects_in_world]=self
        var.number_of_objects_in_world+=1
        
    def change_rotation(self,x,y,z):
        assert(isinstance(x,(int,float)))
        assert(isinstance(y,(int,float)))
        assert(isinstance(z,(int,float)))
        self.angles=[x,y,z]
    def change_x_rotation(self,x):
        assert(isinstance(x,(int,float)))
        self.angles[0]=x
    def change_y_rotation(self,y):
        assert(isinstance(y,(int,float)))
        self.angles[1]=y
    def change_z_rotation(self,z):
        assert(isinstance(z,(int,float)))
        self.angles[2]=z
        
    def change_position(self,x,y,z):
        assert(isinstance(x,(int,float)))
        assert(isinstance(y,(int,float)))
        assert(isinstance(z,(int,float)))
        self.position=[x,y,z]
    def change_x_position(self,x):
        assert(isinstance(x,(int,float)))
        self.position[0]=x
    def change_y_position(self,y):
        assert(isinstance(y,(int,float)))
        self.position[1]=y
    def change_z_position(self,z):
        assert(isinstance(z,(int,float)))
        self.position[2]=z

    def change_position_change(self,x,y,z):
        assert(isinstance(x,(int,float)))
        assert(isinstance(y,(int,float)))
        assert(isinstance(z,(int,float)))
        self.position_change=[x,y,z]
    def change_x_position_change(self,x):
        assert(isinstance(x,(int,float)))
        self.position_change[0]=x
    def change_y_position_change(self,y):
        assert(isinstance(y,(int,float)))
        self.position_change[1]=y
    def change_z_position_change(self,z):
        assert(isinstance(z,(int,float)))
        self.position_change[2]=z

    def change_rotation_change(self,x,y,z):
        assert(isinstance(x,(int,float)))
        assert(isinstance(y,(int,float)))
        assert(isinstance(z,(int,float)))
        self.angles_change=[x,y,z]
    def change_x_rotation_change(self,x):
        assert(isinstance(x,(int,float)))
        self.angles_change[0]=x
    def change_y_rotation_change(self,y):
        assert(isinstance(y,(int,float)))
        self.angles_change[1]=y
    def change_z_rotation_change(self,z):
        assert(isinstance(z,(int,float)))
        self.angles_change[2]=z
    def move_with(self,mover):
        assert(isinstance(mover, objectSuperClass))
        self.move_with_object=True
        self.mover=mover
    def rotate_with(self,rotater):
        assert(isinstance(rotater, objectSuperClass))
        self.rotate_with_object=True
        self.rotater=rotater
        
    
        
    