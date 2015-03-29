from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame
import variables.variables as var
import constants.constants as con
import physMMath.physMMath as Mmath
from OpenGL.raw.GLU import gluLookAt
import time
import numpy as np


def render():
    if var.fps:
        count_fps()
    if var.holding:
        hold()
    update_ignore_set()
    check_for_collisions()
    glMatrixMode(GL_MODELVIEW)
    #clear buffer
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    #load standard matrix
    glLoadIdentity();
    #setup where to look at
    gluLookAt(    var.viewing_position[0], var.viewing_position[1], var.viewing_position[2],
           var.viewing_center[0], var.viewing_center[1],  var.viewing_center[2],
            0.0, 0.0,  1.0)
    #set the background
    glClearColor(var.background_color[0],var.background_color[1],var.background_color[2],var.background_color[3])
    #glPushMatrix()
    #pos = var.light_position
    #direction = [0.0, 0, -1.0]
    #spotAngle = 40
    #glLightfv(GL_LIGHT0, GL_POSITION, pos)
    #glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, spotAngle)
    #glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, direction)
    #glLightf(GL_LIGHT0, GL_SPOT_EXPONENT, 2)
    
    #load all objects
    for i in range(var.number_of_objects_in_world):
        glPushMatrix()
        var.objects_in_world[i].load()
        glPopMatrix()
    
    #exchange buffer
    glutSwapBuffers()
    run_functions()
def add_function_to_mainloop(func):
    assert(callable(func))
    var.functions_to_run_in_mainloop[var.functions_in_mainloop]=func
    var.functions_in_mainloop+=1
def check_for_collisions():
    combinations=Mmath.get_combinations(range(var.number_of_objects_in_world), 2)
    for element in combinations:
        if var.objects_in_world[element[0]].collision_possible(var.objects_in_world[element[1]]):
            handle_collision(element)
def handle_collision(elements):
    if var.objects_in_world[elements[0]].collision_enabled and var.objects_in_world[elements[1]].collision_enabled and objects_have_collided(elements):
        try:
            if var.ignore_set[elements]==0:
                calculate_velocity_after_impact(elements)
        except KeyError:
            var.ignore_set[elements]=int(np.floor(var.holding_fps/10.0))
            calculate_velocity_after_impact(elements)
def update_ignore_set():
    for element in var.ignore_set:
        if var.ignore_set[element]>0:
            var.ignore_set[element]-=1
            
def objects_have_collided(elements):
    boundary_point_one=var.objects_in_world[elements[0]].get_boundary_point(var.objects_in_world[elements[1]])
    boundary_point_two=var.objects_in_world[elements[1]].get_boundary_point(var.objects_in_world[elements[0]])
    #if check_if_objects_inside(elements, boundary_point_one, boundary_point_two):
     #   return False
    temp=Mmath.get_distance_between_points(boundary_point_one, boundary_point_two)<var.distance_for_collision
    return temp

def calculate_velocity_after_impact(elements):
    boundary_point_one=var.objects_in_world[elements[0]].get_boundary_point(var.objects_in_world[elements[1]])
    normal=var.objects_in_world[elements[0]].get_normal(boundary_point_one)
    a1=np.dot(var.objects_in_world[elements[0]].position_change,normal)
    a2=np.dot(var.objects_in_world[elements[1]].position_change,normal)
    optimizedP = (2.0 * (a1 - a2)) / (var.objects_in_world[elements[0]].mass + var.objects_in_world[elements[1]].mass)
    v1_prim= np.array(var.objects_in_world[elements[0]].position_change) - optimizedP * var.objects_in_world[elements[1]].mass * np.array(normal)
    v2_prim= np.array(var.objects_in_world[elements[1]].position_change) + optimizedP * var.objects_in_world[elements[0]].mass * np.array(normal)
    var.objects_in_world[elements[0]].position_change=list(v1_prim)
    var.objects_in_world[elements[1]].position_change=list(v2_prim)
    
    #returns true if p1 is inside elements[0] or p2 is inside elements[1]
def check_if_objects_inside(elements,p1,p2):
    point1=Mmath.calculate_unprojection_point(var.objects_in_world[elements[0]], p2[0], p2[1], p2[2])
    point2=Mmath.calculate_unprojection_point(var.objects_in_world[elements[1]], p1[0], p1[1], p1[2])
    temp=(var.objects_in_world[elements[0]].check_point(point1) and var.objects_in_world[elements[1]].check_point(point2))
    if temp:
        print("elements: "+str(elements[0]) +" is inside object: " +str(elements[1]))
    return temp
def run_functions():
    for i in range(var.functions_in_mainloop):
        var.functions_to_run_in_mainloop[i]()
def hold():
    if var.current_fps>var.holding_fps+var.holding_delta:
        if var.holding_change_time+var.holding_timer<time.time():
            if var.holding_sleep==0.0:
                var.holding_sleep=0.01
            var.holding_sleep*=1.2
            var.holding_change_time=time.time()
    if var.current_fps<var.holding_fps-var.holding_delta:
        if var.holding_change_time+var.holding_timer<time.time():
            if var.holding_sleep==0.0:
                var.holding_sleep=0.01
            var.holding_sleep/=1.2
            var.holding_change_time=time.time()
    time.sleep(var.holding_sleep)
            
        
            
        
def count_fps():
    if var.fps_time+var.fps_timer<time.time():
        var.current_fps=var.fps_counter/(time.time()-var.fps_time)
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
    disable_hold_fps()
def hold_fps(fps):
    assert(isinstance(fps,(int,float)) and fps>0.0)
    enable_fps_counter()
    var.holding=True
    var.holding_fps=fps
def disable_hold_fps():
    var.holding=False
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
    #glTranslatef(var.viewing_position[0],var.viewing_position[1], var.viewing_position[2])
    glMatrixMode(GL_MODELVIEW)