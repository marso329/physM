"""
  Author: Martin Söderén
  Email: martin.soderen@gmail.com
  Date: 2015-03-29
  Description: This is a cubeclass that inherits from the ObjectSuperClass
"""

from objects.objectSuperClass import *
import physMMath.physMMath as Mmath

class cube(objectSuperClass):

    def __init__(self, length, width, height, color):
        assert(self.check_if_float_or_int(length))
        assert(self.check_if_float_or_int(width))
        assert(self.check_if_float_or_int(height))
        objectSuperClass.__init__(self)
        self.index = glGenLists(1)
        #all points in the cube
        self.vertices = {
        0:(1.0, -1.0, -1.0),
        1:(1.0, 1.0, -1.0),
        2:(-1.0, 1.0, -1.0),
        3:(-1.0, -1.0, -1.0),
        4:(1.0, -1.0, 1.0),
        5:(1.0, 1.0, 1.0),
        6:(-1.0, -1.0, 1.0),
        7:(-1.0, 1.0, 1.0)
        }
        self.number_of_edges = 12
        self.number_of_triangles = 12
        #all vectors of the points in self.vertices that create a cube
        self.edges = {
        0:(0, 1),
        1:(0, 3),
        2:(0, 4),
        3:(2, 1),
        4:(2, 3),
        5:(2, 7),
        6:(6, 3),
        7:(6, 4),
        8:(6, 7),
        9:(5, 1),
        10:(5, 4),
        11:(5, 7)
        }
        #all triangles that creates a cube of the points in self.vertices
        self.triangles = {
        0:(4, 7, 6),
        1:(4, 5, 7),
        2:(4, 0, 1),
        3:(4, 1, 5),
        4:(3, 1, 0),
        5:(3, 2, 1),
        6:(6, 7, 2),
        7:(6, 2, 3),
        8:(7, 5, 1),
        9:(7, 1, 2),
        10:(6, 0, 4),
        11:(6, 3, 0)
        }
        #normals to the triangles in self.triangels
        self.normals = {
        0:(0, 0, 1),
        1:(0, 0, 1),
        2:(1, 0, 0),
        3:(1, 0, 0),
        4:(0, 0, -1),
        5:(0, 0, -1),
        6:(-1, 0, 0),
        7:(-1, 0, 0),
        8:(0, 1, 0),
        9:(0, 1, 0),
        10:(0, -1, 0),
        11:(0, -1, 0)
        }
        # 6 planes that create a cube, these are used when calculating collision detection
        self.planes = {
        0:(5, 7, 6),
        1:(3, 0, 1),
        2:(3, 7, 6),
        3:(0, 1, 5),
        4:(3, 6, 4),
        5:(7, 5, 1),
        }
        self.number_of_vertices = 8
        self.check_color(color)
        self.length = length
        self.width = width
        self.height = height
        self.max_distance_from_centre = 0
        self.create()
        self.collision_enabled = True
        
    #recalculates points in self.vertices depending on size of cube
    def create(self):
        for i in range(self.number_of_vertices):
            temp = self.vertices[i]
            temp_new = (temp[0] * self.length / 2.0, temp[1] * self.width / 2.0, temp[2] * self.height / 2.0)
            self.vertices[i] = temp_new
            for element in self.vertices[i]:
                if abs(element) > self.max_distance_from_centre:
                    self.max_distance_from_centre = element
                    
    #loads all information to the GPU
    def load(self):
        if self.first_load:
            self.load_first()
            self.first_load = False
        else:
            self.update_everything()
            glCallList(self.index)
    
    #returns the normal to a point
    def get_normal(self, point):
        temp = Mmath.calculate_unprojection_point(self, point[0], point[1], point[2])
        x = self.length / 2 - 0.01
        y = self.width / 2 - 0.01
        z = self.height / 2 - 0.01
        if temp[0] <= x and temp[0] >= -x and temp[1] <= y and temp[1] >= -y  and temp[2] > 0:
            return Mmath.rotate_point(self, 0, 0, 1)
        if temp[0] <= x and temp[0] >= -x and temp[1] < y and temp[1] >= -y  and temp[2] < 0:
            return Mmath.rotate_point(self, 0, 0, -1)
        if temp[0] > 0  and temp[1] <= y and temp[1] >= -y  and temp[2] >= -z and temp[2] < z:
            return Mmath.rotate_point(self, 1, 0, 0)
        if temp[0] < 0  and temp[1] <= y and temp[1] >= -y  and temp[2] >= -z and temp[2] <= z:
            return Mmath.rotate_point(self, -1, 0, 0)
        if temp[0] >= -x and temp[0] <= x  and temp[1] > 0   and temp[2] >= -z and temp[2] <= z:
            return Mmath.rotate_point(self, 0, 1, 0)
        if temp[0] >= -x and temp[0] <= x  and temp[1] <= 0   and temp[2] >= -z and temp[2] <= z:
            return Mmath.rotate_point(self, 0, -1, 0)
        return (0, 0, 0)
    
    #returns the point which is on the line between both objects centres
    def get_boundary_point(self, object_in_world):
        # line between objects
        line = Mmath.line(self.position, object_in_world.position)
        projection_planes={}
        # calculate new planes:
        for i in range(6):
            point1 = self.vertices[self.planes[i][0]]
            point2 = self.vertices[self.planes[i][1]]
            point3 = self.vertices[self.planes[i][2]]
            point1 = Mmath.calculate_projection_point(self, point1[0], point1[1], point1[2])
            point2 = Mmath.calculate_projection_point(self, point2[0], point2[1], point2[2])
            point3 = Mmath.calculate_projection_point(self, point3[0], point3[1], point3[2])
            projection_planes[i] = Mmath.plane(point1, point2, point3)
        # calculate all the solutions for the line and planes
        solutions = []
        for i in range(6):
            solutions.append(Mmath.get_line_intersection_with_plane(line, projection_planes[i]))
        # find which plane is the right one
        minimum = Mmath.get_distance_between_points(self.position, object_in_world.position)
        index = 0
        for i in range(6):
            if not self.check_solution(solutions[i]):continue
            temp_point = Mmath.calculate_unprojection_point(self, solutions[i][0], solutions[i][1], solutions[i][2])
            if not self.check_point(temp_point):continue
            distance = Mmath.get_distance_between_points(object_in_world.position, solutions[i])
            if distance < minimum:
                minimum = distance
                index = i
        return solutions[index]
    
    # checks so point is inside this object, use  unproject if its a point on the edges
    def check_point(self, point):
        marginal = var.marginal_for_checking_boundary_checking / 2.0
        return abs(point[0]) - marginal < self.length / 2.0 and abs(point[1]) - marginal < self.width / 2.0 and abs(point[2]) - marginal < self.height / 2.0
    
    #checks if a solution for solving line plane equation is reasonable
    def check_solution(self, solution):
        element = solution
        return abs(element[0]) < var.max_value_for_solution and abs(element[1]) < var.max_value_for_solution and abs(element[2]) < var.max_value_for_solution
    
    #creates the calllist the first time load is called
    def load_first(self):
        self.update_everything()
        glNewList(self.index, GL_COMPILE)
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [128 / 256.0, 128 / 256.0, 128 / 256.0, 1.0]);
        glMaterialfv(GL_FRONT, GL_SPECULAR, [1, 1, 1, 1]);
        glMaterialfv(GL_FRONT, GL_SHININESS, [128.0]);        
        if not self.solid:
            glBegin(GL_LINES)
            if not self.transparency_enabled:
                glColor3f(self.color[0], self.color[1], self.color[2])
            else:
                glColor4f(self.color[0], self.color[1], self.color[2], self.transparency)
                
            for i in range(self.number_of_edges):
                for j in range(2):
                    glVertex3fv(self.vertices[self.edges[i][j]])
        else:
            glBegin(GL_TRIANGLES)
            if not self.transparency_enabled:
                glColor3f(self.color[0], self.color[1], self.color[2])
            else:
                glColor4f(self.color[0], self.color[1], self.color[2], self.transparency)
            for i in range(self.number_of_triangles):
                normal = self.normals[i]
                for j in range(3):
                    glNormal(normal[0], normal[1], normal[2])
                    glVertex3fv(self.vertices[self.triangles[i][j]])
        glEnd()
        glEndList()
    
        
