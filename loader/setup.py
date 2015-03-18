#all imports
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import os, sys, inspect
from constants.constants import *
from variables.variables import *
from enviroment.enviroment import *

#add the physM folder to PYTHONPATH
abs_path=os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
sys.path.append(abs_path[:abs_path.rfind("/")])

#initiate pygame
pygame.init()

#setup the display, we use doublebuffer mode
pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), DOUBLEBUF|OPENGL)

#black background
glClearColor(0.0, 0.0, 0.0, 0.0)    # This Will Clear The Background Color To Black

# Enables Clearing Of The Depth Buffer
glClearDepth(1.0)
    
# The Type Of Depth Test To Do
glDepthFunc(GL_LESS)

# Enables Depth Testing
glEnable(GL_DEPTH_TEST)

# Enables Smooth Color Shading
glShadeModel(GL_SMOOTH)
    
#sets which matrix is subject to the following operations
glMatrixMode(GL_PROJECTION)

# Reset The Projection Matrix
glLoadIdentity()

#the initial perspective
gluPerspective(45, (SCREEN_WIDTH/SCREEN_HEIGHT), 0.1, 50.0)

#the initial position for the perspective
glTranslatef(0.0,0.0, -5)

#sets which matrix is subject to the following operations
glMatrixMode(GL_MODELVIEW)

