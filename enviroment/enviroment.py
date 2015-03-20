from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame
import variables.variables as var
import constants.constants as con
from OpenGL.raw.GLU import gluLookAt
import time


def render():
    if var.fps:
        count_fps()
    print(var.current_fps)
    glMatrixMode(GL_MODELVIEW)
    #clear buffer
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    #load standard matrix
    glLoadIdentity();
    #setup where to look at
    gluLookAt(    var.viewing_position[0], var.viewing_position[1], var.viewing_position[2],
           var.viewing_center[0], var.viewing_center[1],  var.viewing_center[2],
            0.0, 1.0,  0.0)
    #set the background
    glClearColor(var.background_color[0],var.background_color[1],var.background_color[2],var.background_color[3])
    #load all objects
    for i in range(var.number_of_objects_in_world):
        glPushMatrix()
        var.objects_in_world[i].load()
        glPopMatrix()
    
    #exchange buffer
    glutSwapBuffers()
def count_fps():
    if var.fps_time+1<time.time():
        var.current_fps=var.fps_counter
        var.fps_time=time.time()
        var.fps_counter=0
    else:
        var.fps_counter+=1
    
def exit_function():
    glutDestroyWindow(var.window)
    sys.exit()
def key_pressed(*args):
    try:
        var.key_bindings[args[0]]()
    except KeyError:
        pass
def enable_fps_counter():
    var.fps=True
def disable_fps_counter():
    var.fps=False

def check_color(color):
    try:
        con.COLORS[color]
    except KeyError:
        color=con.STANDARD_COLOR_STRING
    return color
def set_background_color(color):
    color=check_color(color)
    var.background_color=con.COLORS[color]+(var.background_color[3],)
    var.background_color_string=color
    
def set_background_alpha(alpha):
    assert(isinstance(alpha,float))
    assert(alpha<=1.0 and alpha>=0)
    var.background_color=var.background_color[:3]+(alpha,)
def bind_key(key,func):
    var.key_bindings[key]=func
    
def change_viewing_position(dx,dy,dz):
    temp=(var.viewing_position[0]+dx,var.viewing_position[1]+dy,var.viewing_position[2]+dz)
    var.viewing_position=temp
    
def change_viewing_center(dx,dy,dz):
    temp=(var.viewing_center[0]+dx,var.viewing_center[1]+dy,var.viewing_center[2]+dz)
    var.viewing_center=temp
    
def resize_window(Width, Height):
    if Height == 0:                        # Prevent A Divide By Zero If The Window Is Too Small 
        Height = 1

        # Reset The Current Viewport And Perspective Transformation
    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 50.0)
    glTranslatef(var.viewing_position[0],var.viewing_position[1], var.viewing_position[2])
    glMatrixMode(GL_MODELVIEW)