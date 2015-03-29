from OpenGL.GL import *
from OpenGL.GLU import *
import constants.constants as con
import variables.variables as var
import physMMath.physMMath as Mmath
import inspect
import time
#from OpenGL.GL.VERSION.GL_1_0 import glGetDoublev
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
        self.dt=0.0
        self.time_since_change=time.time()
        self.affected_by_gravity=False
        self.max_distance_from_centre=0
        self.collision_enabled=False
        self.mass=1.0
        self.first_load=True
    def get_line_between_objects(self,object_in_world):
        return Mmath.line(tuple(self.position),tuple(object_in_world.position))
        
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
    def get_boundary_point(self,x,y,z):
        caller = inspect.getouterframes(inspect.currentframe())[1][3]
        raise NotImplementedError(caller + ' must be implemented in subclass')      
    #returns true if it is possible with a collision with the object
    def collision_possible(self,object_in_world):
        collision=True
        for i in range(3):
            if ((self.position[i]+self.max_distance_from_centre<=object_in_world.position[i]-object_in_world.max_distance_from_centre) or 
                (object_in_world.position[i]+object_in_world.max_distance_from_centre<=self.position[i]-self.max_distance_from_centre)):
                collision=False
        return collision  
    
    def update_time(self):
        self.dt=time.time()-self.time_since_change
        self.time_since_change=time.time()
    def update_angels(self):
        if not self.rotate_with_object:
            self.angles[0]+=self.angles_change[0]*self.dt
            self.angles[1]+=self.angles_change[1]*self.dt
            self.angles[2]+=self.angles_change[2]*self.dt
        else:
            self.angles[0]+=(self.angles_change[0]+self.rotater.angles_change[0])*self.dt
            self.angles[1]+=(self.angles_change[1]+self.rotater.angles_change[1])*self.dt
            self.angles[2]+=(self.angles_change[2]+self.rotater.angles_change[2])*self.dt
    def update_position(self):
        if not self.move_with_object:
            self.position[0]+=self.position_change[0]*self.dt
            self.position[1]+=self.position_change[1]*self.dt
            self.position[2]+=self.position_change[2]*self.dt
        else:
            self.position[0]+=(self.position_change[0]+self.mover.position_change[0])*self.dt
            self.position[1]+=(self.position_change[1]+self.mover.position_change[1])*self.dt
            self.position[2]+=(self.position_change[2]+self.mover.position_change[2])*self.dt
    def update_velocity(self):
        self.position_change[0]+=var.gravity_vector[0]*self.dt
        self.position_change[1]+=var.gravity_vector[1]*self.dt
        self.position_change[2]+=var.gravity_vector[2]*self.dt
    def rotate(self):
        glRotatef(self.angles[0], 1.0, 0.0, 0.0)
        glRotatef(self.angles[1], 0.0, 1.0, 0.0)
        glRotatef(self.angles[2], 0.0, 0.0, 1.0)
    def move(self):
        glTranslatef(self.position[0], self.position[1], self.position[2])
    def update_everything(self):
        self.update_time()
        if self.affected_by_gravity:
            self.update_velocity()
        self.update_angels()
        self.update_position()
        self.move()
        self.rotate()
    def enable_gravity(self):
        self.affected_by_gravity=True
    def disable_gravity(self):
        self.affected_by_gravity=False
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
        
    def change_angular_displacement(self,x,y,z):
        assert(isinstance(x,(int,float)))
        assert(isinstance(y,(int,float)))
        assert(isinstance(z,(int,float)))
        self.angles=[x,y,z]
    def change_x_angular_displacement(self,x):
        assert(isinstance(x,(int,float)))
        self.angles[0]=x
    def change_y_angular_displacement(self,y):
        assert(isinstance(y,(int,float)))
        self.angles[1]=y
    def change_z_angular_displacement(self,z):
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

    def change_velocity(self,x,y,z):
        assert(isinstance(x,(int,float)))
        assert(isinstance(y,(int,float)))
        assert(isinstance(z,(int,float)))
        self.position_change=[x,y,z]
    def change_x_velocity(self,x):
        assert(isinstance(x,(int,float)))
        self.position_change[0]=x
    def change_y_velocity(self,y):
        assert(isinstance(y,(int,float)))
        self.position_change[1]=y
    def change_z_velocity(self,z):
        assert(isinstance(z,(int,float)))
        self.position_change[2]=z

    def change_angular_velocity(self,x,y,z):
        assert(isinstance(x,(int,float)))
        assert(isinstance(y,(int,float)))
        assert(isinstance(z,(int,float)))
        self.angles_change=[x,y,z]
    def change_x_angular_velocity(self,x):
        assert(isinstance(x,(int,float)))
        self.angles_change[0]=x
    def change_y_angular_velocity(self,y):
        assert(isinstance(y,(int,float)))
        self.angles_change[1]=y
    def change_z_angular_velocity(self,z):
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
        
    
        
    