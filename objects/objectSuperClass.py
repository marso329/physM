"""
  Author: Martin Söderén
  Email: martin.soderen@gmail.com
  Date: 2015-03-29
  Description: This is the ObjectSuperClass. All object must inherit from this class
"""


from OpenGL.GL import *
from OpenGL.GLU import *
import constants.constants as con
import variables.variables as var
import physMMath.physMMath as Mmath
import inspect
import time
import numpy as np
from enviroment.enviroment import add_function_to_mainloop

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
        self.move_queue=[]
        self.moving=False
        self.move_to_position=(0,0,0)
        
    #returns a line instance of a line between self and object_in_world
    def get_line_between_objects(self,object_in_world):
        return Mmath.line(tuple(self.position),tuple(object_in_world.position))
        
    #set the transparency of this object to a value between 0 and 1.0
    def set_transparency(self,trans):
        assert(isinstance(trans, (float,int)) and trans<=1.0 and trans>=0)
        self.transparency=trans
        self.transparency_enabled=True
        
    #Subclasses must have own load function
    def load(self):
        caller = inspect.getouterframes(inspect.currentframe())[1][3]
        raise NotImplementedError(caller + ' must be implemented in subclass')
    
    #moves x,y,z relative to current position
    def move_relative(self,x,y,z,v):
        temp=self.position
        self.move_to(temp[0]+x, temp[1]+y, temp[2]+z, v)
        
    #moves to x,y,z with velocity v
    def move_to(self,x,y,z,v):
        assert(isinstance(v,(int,float)))
        assert(v>0)
        if self.moving:
            self.move_queue.append((x,y,z,v))
            return
        
        self.moving=True
        direction=(x-self.position[0],y-self.position[1],z-self.position[2])
        if direction[0]!=0:
            v1=v/(np.sqrt(1+direction[1]**2/direction[0]**2+direction[2]**2/direction[0]**2))
            v2=v1*direction[1]/direction[0]
            v3=v1*direction[2]/direction[0]
        elif direction[1]!=0:
            v2=v/(np.sqrt(1+direction[0]**2/direction[1]**2+direction[2]**2/direction[1]**2))
            v1=v2*direction[0]/direction[1]
            v3=v2*direction[2]/direction[1]
        elif direction[2]!=0:
            v3=v/(np.sqrt(1+direction[1]**2/direction[2]**2+direction[0]**2/direction[2]**2))
            v2=v3*direction[1]/direction[2]
            v1=v3*direction[0]/direction[2]
        else:
            return
        if direction[0]!=0:
            v1=v1*(direction[0]/abs(direction[0]))
        if direction[1]!=0:
            v2=v2*(direction[1]/abs(direction[1]))
        if direction[2]!=0:
            v3=v3*(direction[2]/abs(direction[2]))
        self.position_change=(v1,v2,v3)
        self.move_to_position=(x,y,z)
        def checker():
            collision=True
            for i in range(3):
                if ((self.position[i]+var.distance_for_collision<=self.move_to_position[i]-var.distance_for_collision) or 
                (self.move_to_position[i]+var.distance_for_collision<=self.position[i]-var.distance_for_collision)):
                    collision=False
            if collision:
                self.position_change=(0,0,0)
                var.functions_to_run_in_mainloop[self.check_function]=lambda:None
                if len(self.move_queue):
                    temp=self.move_queue[0]
                    self.move_queue.pop(0)
                    self.moving=False
                    self.move_to(temp[0], temp[1], temp[2], temp[3])
                self.moving=False
        add_function_to_mainloop(checker)
        self.check_function=var.functions_in_mainloop-1
            
    
    #Subclasses does not need this one, it is voluntary
    def create(self):
        caller = inspect.getouterframes(inspect.currentframe())[1][3]
        raise NotImplementedError(caller + ' must be implemented in subclass')
    
    #if the subclass wants to use collision detection this is necessary.
    def get_boundary_point(self,object_in_world):
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
            temp=list(self.move_to_position)
            temp[0]+=(self.mover.position_change[0])*self.dt
            temp[1]+=(self.mover.position_change[1])*self.dt
            temp[2]+=(self.mover.position_change[2])*self.dt
            self.move_to_position=tuple(temp)
            for i in range(len(self.move_queue)):
                temp=list(self.move_queue[i])
                temp[0]+=(self.mover.position_change[0])*self.dt
                temp[1]+=(self.mover.position_change[1])*self.dt
                temp[2]+=(self.mover.position_change[2])*self.dt
                self.move_queue[i]=tuple(temp)
                
    
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
        
    
        
    