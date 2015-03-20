#OpenGL imports
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#For adding PhysM to PYTHONPATH
import os, sys, inspect

#global variables and constants
import constants.constants as con
import variables.variables as var
from enviroment.enviroment import *
from constants.constants import ESCAPE

#add the physM folder to PYTHONPATH
abs_path=os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
sys.path.append(abs_path[:abs_path.rfind("/")])


#Initiate GLUT for the windowhandling
glutInit("")

glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA )

glutInitWindowSize(con.SCREEN_WIDTH, con.SCREEN_HEIGHT)


glutInitWindowPosition(0, 0)


var.window = glutCreateWindow("PhysM")

#black background
glClearColor(0.0, 0.0, 0.0, 0.0)    # This Will Clear The Background Color To Black

# Enables Clearing Of The Depth Buffer
glClearDepth(1.0)
    
# The Type Of Depth Test To Do
glDepthFunc(GL_LESS)

# Enables Depth Testing
glEnable(GL_DEPTH_TEST)

# enable transpercy
glEnable(GL_BLEND)

# Enables Smooth Color Shading
glShadeModel(GL_SMOOTH)

glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
#sets which matrix is subject to the following operations
glMatrixMode(GL_PROJECTION)

# Reset The Projection Matrix
glLoadIdentity()

#the initial perspective
gluPerspective(50, (con.SCREEN_WIDTH/con.SCREEN_HEIGHT), 0.1, 50.0)

#the initial position for the perspective
#glTranslatef(var.viewing_position[0],var.viewing_position[1], var.viewing_position[2])

#sets which matrix is subject to the following operations
glMatrixMode(GL_MODELVIEW)


glutKeyboardFunc(key_pressed)
glutSpecialFunc(key_pressed)

glutDisplayFunc(render)

glutIdleFunc(render)

#glutReshapeFunc(resize_window)
bind_key(ESCAPE, exit_function)

