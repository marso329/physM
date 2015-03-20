from objects.objectSuperClass import *
from constants.constants import PRIMITIVE_LOOKUP
from xdg.BaseDirectory import load_first_config
class objectFile(objectSuperClass):

    def __init__(self,filename):
        objectSuperClass.__init__(self)
        self.vertices={}
        self.index = glGenLists(1)
        self.number_of_vertices=1
        self.primitive=None
        self.primitive_set=False
        self.primitive_number=0
        self.faces={}
        self.first_load=True
        self.number_of_faces=0
        for line in open(filename,"r"):
            if line.startswith('#'): continue
            values=line.split()
            if not values: continue
            if values[0]=="v":
                v=list(map(float,values[1:4]))
                v=v[0],v[1],v[2]
                self.vertices[self.number_of_vertices]=v
                self.number_of_vertices+=1
            if values[0]=="f":
                values=values[1:]
                if not self.primitive_set:
                    self.set_primitive(len(values))
                assert(len(values)==self.primitive_number)
                v=list(map(int,values[:self.primitive_number]))
                temp=()
                for i in range(self.primitive_number):
                    temp=temp+(v[i],)
                self.faces[self.number_of_faces]=temp
                self.number_of_faces+=1
        self.add_to_world()
    def load(self):
        if self.first_load:
            self.load_first()
            self.first_load=False
        else:
            self.update_everything()
            glCallList(self.index)
    def load_first(self):
        self.update_everything()
        glNewList(self.index, GL_COMPILE) 
        glBegin(self.primitive)
        if not self.transparency_enabled:
            glColor3f(self.color[0],self.color[1],self.color[2])
        else:
            glColor4f(self.color[0],self.color[1],self.color[2],self.transparency)
        for i in range(self.number_of_faces):
            for j in range(self.primitive_number):
                glVertex3fv(self.vertices[self.faces[i][j]])
        glEnd()
        glEndList()
                
                     
    def set_primitive(self,x):
        self.primitive=PRIMITIVE_LOOKUP[x]
        self.primitive_set=True  
        self.primitive_number=x  
                
                
                
                
            
            
            
            
            