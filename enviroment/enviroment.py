from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
import variables.variables as variables
def render():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    for i in range(variables.number_of_objects_in_world):
        variables.objects_in_world[i].load()
    pygame.display.flip()
    pygame.time.wait(10)
        