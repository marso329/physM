from OpenGL.GL import *
from OpenGL.GLU import *
from constants.constants import *    
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
            COLORS[color]
        except KeyError:
            color=STANDARD_COLOR
    def check_if_float_or_int(self,value):
        return isinstance(value,(int, long,float))
        
    