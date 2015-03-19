from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame
import variables.variables as var
import constants.constants as con

def render():
    glRotatef(1, 3, 1, 1)
    glClearColor(var.background_color[0],var.background_color[1],var.background_color[2],var.background_color[3])
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    for i in range(var.number_of_objects_in_world):
        var.objects_in_world[i].load()
    glutSwapBuffers()
    
def keyPressed(*args):
    if args[0] == con.ESCAPE:
        glutDestroyWindow(var.window)
        sys.exit()
def set_background_color(color):
    var.background_color=con.COLORS[color]+(var.background_color[3],)
def set_background_alpha(alpha):
    assert(isinstance(alpha,float))
    assert(alpha<=1.0 and alpha>=0)
    var.background_color=var.background_color[:3]+(alpha,)