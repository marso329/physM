from objects.objectSuperClass import *
from objects import sphere
import physMMath.physMMath as Mmath
import numpy as np
from physMMath.physMMath import dot_product
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
        self.check_color(color)
        self.length=length
        self.width=width
        self.height=height
        self.first_load=True
        self.max_distance_from_centre=0
        self.create()
        self.collision_enabled=True
        self.last_normal=[0,0,0]
    def create(self):
        for i in range(self.number_of_vertices):
            temp=self.vertices[i]
            temp_new=(temp[0]*self.length/2.0,temp[1]*self.width/2.0,temp[2]*self.height/2.0)
            self.vertices[i]=temp_new
            for element in self.vertices[i]:
                if abs(element)>self.max_distance_from_centre:
                    self.max_distance_from_centre=element
        
            
    def load(self):
        if self.first_load:
            self.load_first()
            self.first_load=False
        else:
            self.update_everything()
            glCallList(self.index)
    def get_normal(self,point):
        temp=Mmath.calculate_unprojection_point(self, point[0], point[1], point[2])
        x=self.length/2-0.01
        y=self.width/2-0.01
        z=self.height/2-0.01
        if temp[0]<=x and temp[0]>=-x and temp[1]<=y and temp[1]>=-y  and temp[2]>0:
            return (0,0,1)
        if temp[0]<=x and temp[0]>=-x and temp[1]<y and temp[1]>=-y  and temp[2]<0:
            return (0,0,-1)
        if temp[0]>0  and temp[1]<=y and temp[1]>=-y  and temp[2]>=-z and temp[2]<z:
            return (1,0,0)
        if temp[0]<0  and temp[1]<=y and temp[1]>=-y  and temp[2]>=-z and temp[2]<=z:
            return (-1,0,0)
        
        if temp[0]>=-x and temp[0]<=x  and temp[1]>0   and temp[2]>=-z and temp[2]<=z:
            return (0,1,0)
        if temp[0]>=-x and temp[0]<=x  and temp[1]<=0   and temp[2]>=-z and temp[2]<=z:
            return (0,-1,0)
        return (0,0,0)
        
        
        
        
        
        #return Mmath.normalize_vector(self.last_normal[0],self.last_normal[1],self.last_normal[2])
    #(x,y,z) is a in space, this function return this elements boundary point that is on the line between this point and
    #the elements centre 
    def get_boundary_point(self,object_in_world):
        #line between objects
        line=Mmath.line(self.position,object_in_world.position)
        #calculate new planes:
        for i in range(6):
            point1=self.vertices[self.planes[i][0]]
            point2=self.vertices[self.planes[i][1]]
            point3=self.vertices[self.planes[i][2]]
            point1=Mmath.calculate_projection_point(self, point1[0], point1[1], point1[2])
            point2=Mmath.calculate_projection_point(self, point2[0], point2[1], point2[2])
            point3=Mmath.calculate_projection_point(self, point3[0], point3[1], point3[2])
            self.projection_planes[i]=Mmath.plane(point1,point2,point3)
        #calculate all the solutions for the line and planes
        solutions=[]
        for i in range(6):
            solutions.append(Mmath.get_line_intersection_with_plane(line, self.projection_planes[i]))
        #find which plane is the right one
        min=Mmath.get_distance_between_points(self.position, object_in_world.position)
        index=0
        for i in range(6):
            if not self.check_solution(solutions[i]):continue
            temp_point=Mmath.calculate_unprojection_point(self, solutions[i][0], solutions[i][1], solutions[i][2])
            if not self.check_point(temp_point):continue
            distance=Mmath.get_distance_between_points(object_in_world.position,solutions[i])
            if distance<min:
                min=distance
                index=i
        self.last_normal=self.projection_planes[index].normal
        return solutions[index]
    #checks so point is inside this object, use  unproject if its a point on the edges
    def check_point(self,point):
        marginal=var.marginal_for_checking_boundary_checking/2.0
        return abs(point[0])-marginal<self.length/2.0 and abs(point[1])-marginal<self.width/2.0 and abs(point[2])-marginal<self.height/2.0
    def check_solution(self,solution):
        element=solution
        return abs(element[0])<var.max_value_for_solution and abs(element[1])<var.max_value_for_solution and abs(element[2])<var.max_value_for_solution
    def load_first(self):
        self.update_everything()
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
    
        
