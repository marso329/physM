from objects.objectSuperClass import *
class line(objectSuperClass):

    def __init__(self,p1,p2,color):
        objectSuperClass.__init__(self)
        self.check_color(color)
        self.quadratic = gluNewQuadric()
        gluQuadricNormals(self.quadratic, GLU_SMOOTH)  
        gluQuadricTexture(self.quadratic, GL_TRUE)
        self.first_load=True
        self.index = glGenLists(1)
        self.collision_enabled=False
        self.points=(p1,p2)
        
    def load(self):
        glBegin(GL_LINES)
        for i in range(len(self.points)):
            glVertex3fv(self.points[i])
        glEnd()
            
        