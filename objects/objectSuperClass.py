from OpenGL.GL import *
from OpenGL.GLU import *
import constants.constants as con
import variables.variables as var
import inspect
class objectSuperClass:
    color=(1.0,1.0,1.0)
    solid=False
    def __init__(self):
        pass
    def load(self):
        caller = inspect.getouterframes(inspect.currentframe())[1][3]
        raise NotImplementedError(caller + ' must be implemented in subclass')
    def create(self):
        caller = inspect.getouterframes(inspect.currentframe())[1][3]
        raise NotImplementedError(caller + ' must be implemented in subclass')
    
    def check_color(self,color):
        try:
            self.color=con.COLORS[color]
        except KeyError:
            self.color=con.STANDARD_COLOR
    def check_if_float_or_int(self,value):
        return isinstance(value,(int, long,float))
    def set_solid(self):
        self.solid=True
    #adds itself to the world
    def add_to_world(self):
        var.objects_in_world[var.number_of_objects_in_world]=self
        var.number_of_objects_in_world+=1
    
        
    