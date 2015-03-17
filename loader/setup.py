import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import os, sys, inspect
#add the physM folder to PYTHONPATH
abs_path=os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
sys.path.append(abs_path[:abs_path.rfind("/")])