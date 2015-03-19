from objects.objectSuperClass import *
class cube(objectSuperClass):

    def __init__(self,length,width,height,color):
        assert(self.check_if_float_or_int(length))
        assert(self.check_if_float_or_int(width))
        assert(self.check_if_float_or_int(height))
        objectSuperClass.__init__(self)
        self.vertices={
        0:(1.0, -1.0, -1.0),
        1:(1.0, 1.0, -1.0),
        2:(-1.0, 1.0, -1.0),
        3:(-1.0, -1.0, -1.0),
        4:(1.0, -1.0, 1.0),
        5:(1.0, 1.0, 1.0),
        6:(-1.0, -1.0, 1.0),
        7:(-1.0, 1.0, 1.0)
        }
        #not used yet
        self.X_LOWER=[3,2,6,7]
        self.Y_LOWER=[6,4,3,0]
        self.Z_LOWER=[3,0,1,2]
        self.number_of_edges=12
        self.number_of_triangles=12
        self.edges = {
        0:(0,1),
        1:(0,3),
        2:(0,4),
        3:(2,1),
        4:(2,3),
        5:(2,7),
        6:(6,3),
        7:(6,4),
        8:(6,7),
        9:(5,1),
        10:(5,4),
        11:(5,7)
        }
        self.triangles={0:(4,7,6),
                   1:(4,5,7),
                   2:(4,0,1),
                   3:(4,1,5),
                   4:(3,1,0),
                   5:(3,2,1),
                   6:(6,7,2),
                   7:(6,2,3),
                   8:(7,5,1),
                   9:(7,2,2),
                   10:(6,0,4),
                   11:(6,3,0)
                   }
        self.number_of_vertices=8
        self.length=0
        self.width=0
        self.height=0
        self.check_color(color)
        self.length=length
        self.width=width
        self.height=height
        self.create()
        self.add_to_world()
        #super(objectSuperClass, self).__init__()
    def create(self):
        for i in range(self.number_of_vertices):
            temp=self.vertices[i]
            temp_new=(temp[0]*self.length/2.0,temp[1]*self.width/2.0,temp[2]*self.height/2.0)
            self.vertices[i]=temp_new
            
    def load(self):
        self.update_everything()        
        if not self.solid:
            glBegin(GL_LINES)
            if not self.transparency_enabled:
                glColor3f(self.color[0],self.color[1],self.color[2])
            else:
                glColor4f(self.color[0],self.color[1],self.color[2],self.transparency)
                
            for i in range(self.number_of_edges):
                for j in range(2):
                    glVertex3fv(self.vertices[self.edges[i][j]])
        else:
            glBegin(GL_TRIANGLES)
            if not self.transparency_enabled:
                glColor3f(self.color[0],self.color[1],self.color[2])
            else:
                glColor4f(self.color[0],self.color[1],self.color[2],self.transparency)
            for i in range(self.number_of_triangles):
                for j in range(3):
                    glVertex3fv(self.vertices[self.triangles[i][j]])
            
        glEnd()
    
        