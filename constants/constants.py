
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.raw.GL.ARB.tessellation_shader import GL_TRIANGLES
#Fell free to add more colors
COLORS = {
u'BLUE': (0.0, 0.0, 1.0),
u'WHITE': (1.0, 1.0, 1.0),
u'GREEN': (0.0, 0.5, 0.0),
u'YELLOW': (0.75, 0.75, 0),
u'BLACK': (0.0, 0.0, 0.0),
u'RED': (1.0, 0.0, 0.0), 
u'MAGENTA': (0.75, 0, 0.75)
}
PRIMITIVE_LOOKUP={3:GL_TRIANGLES
                  }

lights={0:GL_LIGHT0,
        1:GL_LIGHT1,
        2:GL_LIGHT2,
        3:GL_LIGHT3,
        4:GL_LIGHT4,
        5:GL_LIGHT5,
        6:GL_LIGHT6,
        7:GL_LIGHT7,}

#standardcolor used then the color is not in the COLOR dict 
STANDARD_COLOR=COLORS["BLACK"]
STANDARD_COLOR_STRING="BLACK"

SCREEN_WIDTH=800
SCREEN_HEIGHT=600

#keybindings
ESCAPE = b'\x1b'

F1=GLUT_KEY_F1
F2=GLUT_KEY_F2
F3=GLUT_KEY_F3
F4=GLUT_KEY_F4
F5=GLUT_KEY_F5
F6=GLUT_KEY_F6
F7=GLUT_KEY_F7
F8=GLUT_KEY_F8
F9=GLUT_KEY_F9
F10=GLUT_KEY_F10
F11=GLUT_KEY_F11
F12=GLUT_KEY_F12
LEFT=GLUT_KEY_LEFT
RIGHT=GLUT_KEY_RIGHT
UP=GLUT_KEY_UP
DOWN=GLUT_KEY_DOWN
PAGE_UP=GLUT_KEY_PAGE_UP
PAGE_DOWN=GLUT_KEY_PAGE_DOWN
KEY_HOME=GLUT_KEY_HOME
END=GLUT_KEY_END
INSERT=GLUT_KEY_INSERT