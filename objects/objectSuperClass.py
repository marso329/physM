from OpenGL.GL import *
from OpenGL.GLU import *
import constants.constants as constants
import variables.variables as variables
import inspect
class objectSuperClass:
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
            constants.COLORS[color]
        except KeyError:
            color=constants.STANDARD_COLOR
    def check_if_float_or_int(self,value):
        return isinstance(value,(int, long,float))
    #adds itself to the world
    def add_to_world(self):
        variables.objects_in_world[variables.number_of_objects_in_world]=self
        variables.number_of_objects_in_world+=1
        
    