#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from numpy import *

lightPosition = np.array([10, 30, 20, 1])
view_rotation = np.array([0, 0, 0])

def init():
    globAmb = [0.3, 0.3, 0.3, 1.0]
    lightAmb = [0.0, 0.0, 0.0, 1.0]
    lightDifAndSpec = [0.7, 0.7, 0.7, 1.0]

    glutInit()

    glClearColor(0.0, 0.0, 0.0, 0.0)

    glEnable(GL_DEPTH_TEST)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)

    glShadeModel(GL_SMOOTH)

    glEnable(GL_LIGHTING)
    glLightfv(GL_LIGHT0, GL_AMBIENT, lightAmb)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightDifAndSpec)
    glLightfv(GL_LIGHT0, GL_SPECULAR, lightDifAndSpec)
    glEnable(GL_LIGHT0)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, globAmb)
    glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE)

    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)


def display():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    gluLookAt(0.0, 40.0, 40.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);

    glRotatef(view_rotation[0], 1.0, 0.0, 0.0)
    glRotatef(view_rotation[1], 0.0, 1.0, 0.0)
    glRotatef(view_rotation[2], 0.0, 0.0, 1.0)

    glPushMatrix()
    pos = [0, 20, 0, 1]
    direction = [0.0, -1.0, 0.0]
    spotAngle = 20
    glLightfv(GL_LIGHT0, GL_POSITION, pos)
    glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, spotAngle)
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, direction)
    glLightf(GL_LIGHT0, GL_SPOT_EXPONENT, 2)

    glPushMatrix();
    glDisable(GL_LIGHTING)
    glTranslate(pos[0], 0.5* pos[1], pos[2])
    glRotatef(-90.0, 1.0, 0.0, 0.0)
    glColor3f(1.0, 1.0, 1.0)
    PI = 3.141592
    glutWireCone(3.0 * np.tan( spotAngle/180.0 * PI ), pos[1], 10, 6)
    glEnable(GL_LIGHTING)
    glPopMatrix();

    draw_cube()

    glPopMatrix()
    glFlush ()


def reshape(w, h):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(w) / float(h), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def keyboard(key, x, y):
    print(key[0])
    if key == chr(27):
        sys.exit(0)
    elif key == 'w':
        view_rotation[0] += 10
        display()
    elif key == 's':
        view_rotation[0] -= 10
        display()
    elif key == 'a':
        view_rotation[1] -= 10
        display()
    elif key == 'd':
        view_rotation[1] += 10
        display()

def draw_cube ():
    glPushMatrix()
    glRotatef(45, 0, 1, 0)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [183/256.0, 65/256.0, 14/256.0, 1.0]);
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1, 1, 1, 1]);
    glMaterialfv(GL_FRONT, GL_SHININESS, [100.0]);
    sz = 10
    step = 1
    for x in range(-sz, sz, step):
        for z in range(-sz, sz, step):

            v0 = np.array([x,  sz, z])
            v1 = np.array([x,  sz, z+step])
            v2 = np.array([x+step,  sz, z+step])
            v3 = np.array([x+step,  sz, z])

            #glBegin(GL_QUADS) # Uncomment to get the surface instead of lines.
            glBegin(GL_LINE_STRIP)

            n = get_normal_vector(v0, v1, v3)
            glNormal(n[0], n[1], n[2])
            glVertex3f(v0[0], v0[1], v0[2])

            n = get_normal_vector(v1, v2, v0)
            glNormal(n[0], n[1], n[2])
            glVertex3f(v1[0], v1[1], v1[2])

            n = get_normal_vector(v2, v3, v1)
            glNormal(n[0], n[1], n[2])
            glVertex3f(v2[0], v2[1], v2[2])

            n = get_normal_vector(v3, v0, v2)
            glNormal(n[0], n[1], n[2])
            glVertex3f(v3[0], v3[1], v3[2])
            glEnd()

    glPopMatrix()




def get_normal_vector (v1, v2, v3):
    v = np.cross(v2-v1, v3-v1)
    n = np.sqrt(np.dot(v, v.conj()))
    if n:
        return v/n 
    else:
        sys.exit(-1)


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(800, 800)
glutInitWindowPosition(300, 0)
glutCreateWindow('Lines')
init()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutMainLoop()