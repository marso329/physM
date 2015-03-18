from objects.objectSuperClass import *
class cube(objectSuperClass):
    primitive=GL_LINES
    vertices={
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
    X_LOWER=[3,2,6,7]
    Y_LOWER=[6,4,3,0]
    Z_LOWER=[3,0,1,2]
    number_of_edges=12
    edges = {
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
    number_of_vertices=8
    length=0
    width=0
    height=0
    def __init__(self,length,width,height,color):
        assert(self.check_if_float_or_int(length))
        assert(self.check_if_float_or_int(width))
        assert(self.check_if_float_or_int(height))
        self.check_color(color)
        self.length=length
        self.width=width
        self.height=height
        self.create()
        self.add_to_world()
    
    def create(self):
        for i in range(self.number_of_vertices):
            temp=self.vertices[i]
            temp_new=(temp[0]*self.length/2.0,temp[1]*self.width/2.0,temp[2]*self.height/2.0)
            self.vertices[i]=temp_new
            
                
        
    def load(self):
        glBegin(GL_LINES)
        for i in range(self.number_of_edges):
            for j in range(2):
                glVertex3fv(self.vertices[self.edges[i][j]])
        glEnd()
    
        