from objects.objectSuperClass import *
class cylinder(objectSuperClass):

    def __init__(self,radius,height,color):
        assert(isinstance(radius, (int,float)) and radius>0.0)
        assert(isinstance(height, (int,float)) and height>0.0)
        objectSuperClass.__init__(self)
        self.check_color(color)
        self.quadratic = gluNewQuadric()
        gluQuadricNormals(self.quadratic, GLU_SMOOTH)  
        gluQuadricTexture(self.quadratic, GL_TRUE)
        self.first_load=True
        self.radius=radius
        self.height=height
        self.max_distance_from_centre=max(radius,height)
        self.index = glGenLists(1)
    def load_first(self):
        self.update_everything()
        glNewList(self.index, GL_COMPILE)
        if not self.transparency_enabled:
            glColor3f(self.color[0],self.color[1],self.color[2])
        else:
            glColor4f(self.color[0],self.color[1],self.color[2],self.transparency)
            
        gluCylinder(self.quadratic,self.radius,self.radius,self.height,32,32)    
        glEndList()
    def load(self):
        if self.first_load:
            self.load_first()
            self.first_load=False
        else:
            self.update_everything()
            glCallList(self.index)
        