from objects.objectSuperClass import *
import physMMath.physMMath as Mmath
import numpy as np
class cube(objectSuperClass):

    def __init__(self,length,width,height,color):
        assert(self.check_if_float_or_int(length))
        assert(self.check_if_float_or_int(width))
        assert(self.check_if_float_or_int(height))
        objectSuperClass.__init__(self)
        self.index = glGenLists(1)
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
        #used for colission detection
        
        self.planes={0:(5,7,6),
                     1:(3,0,1),
                     2:(3,7,6),
                     3:(0,1,5),
                     4:(3,6,4),
                     5:(7,5,1),
                     }
        self.projection_planes={}
        self.number_of_vertices=8
        self.length=0
        self.width=0
        self.height=0
        self.check_color(color)
        self.length=length
        self.width=width
        self.height=height
        self.first_load=True
        self.max_distance_from_centre=0
        self.create()
    def create(self):
        for i in range(self.number_of_vertices):
            temp=self.vertices[i]
            temp_new=(temp[0]*self.length/2.0,temp[1]*self.width/2.0,temp[2]*self.height/2.0)
            self.vertices[i]=temp_new
            for element in self.vertices[i]:
                if element>self.max_distance_from_centre:
                    self.max_distance_from_centre=element
            
    def load(self):
        if self.first_load:
            self.load_first()
            self.first_load=False
        else:
            self.update_everything()
            self.update_projection_planes()
            self.move()
            self.rotate()
            glCallList(self.index)
    #(x,y,z) is a in space, this function return this elements boundary point that is on the line between this point and
    #the elements centre 
    def get_boundary_point(self,object_in_world):
        #the objects centre point projected
        p1=gluProject(object_in_world.position[0],object_in_world.position[1],object_in_world.position[2])
        #this objects centre point
        p2=gluProject(self.position[0],self.position[1],self.position[2])
        #a line between these objects
        line=Mmath.line(p1,p2)
        #calculate al normalds for this object
        temp_normals=[]
        for i in range(6):
            temp_normals.append(np.array(self.projection_planes[i].normal)/sum(self.projection_planes[i].normal))
        #calulcate the greatest dot product of a planes
        temp_dot_products=[]
        line_direction=[p1[0]-p2[0],p1[1]-p2[1],p1[2]-p2[2]]
        line_direction=np.array(line_direction)/sum(line_direction)
        for i in range(6):
            temp_dot_products.append(np.dot(temp_normals[i],line_direction))
        #returns the point on the plane with the greatest dot product 
        temp= Mmath.get_line_intersection_with_plane(line, self.projection_planes[temp_dot_products.index(max(temp_dot_products))])
        return gluUnProject(temp[0],temp[1],temp[2])
    def update_projection_planes(self):
        for i in range(6):
            temp_vertex=self.vertices[self.planes[i][0]]
            p1=gluProject(temp_vertex[0],temp_vertex[1],temp_vertex[2])
            
            temp_vertex=self.vertices[self.planes[i][1]]
            p2=gluProject(temp_vertex[0],temp_vertex[1],temp_vertex[2])
            
            temp_vertex=self.vertices[self.planes[i][2]]
            p3=gluProject(temp_vertex[0],temp_vertex[1],temp_vertex[2])
            self.projection_planes[i]=Mmath.plane(p1,p2,p3)
    
    def load_first(self):
        self.update_everything()
        self.update_projection_planes()
        glNewList(self.index, GL_COMPILE)        
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
        glEndList()
    
        
