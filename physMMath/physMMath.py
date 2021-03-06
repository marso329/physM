import numpy as np
import itertools
from math import sqrt
import variables.variables as var

class plane():
    def __init__(self,p1,p2,p3):
        self.normal=calc_plane(p1, p2, p3)
        self.p1=p1
        self.p2=p2
        self.p3=p3
        self.d=p1[0]*self.normal[0]+p1[1]*self.normal[1]+p1[2]*self.normal[2]
class line():
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2
        self.line=p1[0]-p2[0],p1[1]-p2[1],p1[2]-p2[2]
        

class sphere():
    def __init__(self,centre_point,R):
        self.centre=centre_point
        self.radius=R
#takes in three points and calculates
def calc_plane(v1,v2,v3):
    x=[v1[0],v2[0],v3[0]]
    y=[v1[1],v2[1],v3[1]]
    z=[v1[2],v2[2],v3[2]]
    a = np.column_stack((x, y, z))
    return list(np.linalg.lstsq(a, np.ones_like(x))[0])

def calculate_rotation_matrix(object_in_world):
    x_cos=np.cos(np.radians(object_in_world.angles[0]))
    y_cos=np.cos(np.radians(object_in_world.angles[1]))
    z_cos=np.cos(np.radians(object_in_world.angles[2]))
    
    x_sin=np.sin(np.radians(object_in_world.angles[0]))
    y_sin=np.sin(np.radians(object_in_world.angles[1]))
    z_sin=np.sin(np.radians(object_in_world.angles[2]))
    
    x_matrix=np.matrix([[1,0,0],[0,x_cos,-x_sin],[0,x_sin,x_cos]])
    
    y_matrix=np.matrix([[y_cos,0,y_sin],[0,1,0],[-y_sin,0,y_cos]])
    
    z_matrix=np.matrix([[z_cos,-z_sin,0],[z_sin,z_cos,0],[0,0,1]])
    
    temp_matrix=z_matrix.dot(y_matrix)
    
    return temp_matrix.dot(x_matrix)

def calculate_projection_point(object_in_world,x,y,z):
    temp=np.matrix([[x],[y],[z]])
    rotation_matrix=calculate_rotation_matrix(object_in_world)
    temp=rotation_matrix.dot(temp)
    for i in range(3):
        temp[i]+=object_in_world.position[i]
    temp=temp.tolist()
    return temp[0][0],temp[1][0],temp[2][0]

def rotate_point(object_in_world,x,y,z):
    temp=np.matrix([[x],[y],[z]])
    rotation_matrix=calculate_rotation_matrix(object_in_world)
    temp=rotation_matrix.dot(temp)
    temp=temp.tolist()
    return temp[0][0],temp[1][0],temp[2][0]    

def calculate_unprojection_point(object_in_world,x,y,z):
    temp=np.matrix([[x-object_in_world.position[0]],[y-object_in_world.position[1]],[z-object_in_world.position[2]]])
    rotation_matrix=calculate_rotation_matrix(object_in_world)
    rotation_matrix_inv=np.linalg.inv(rotation_matrix)
    rotation_matrix_inv.dot(temp)
    temp=temp.tolist()
    return temp[0][0],temp[1][0],temp[2][0]
    
    
    

# takes a vector (tuple of 2 points, each with a tuple of 3 coordinates)
# and a tuple of three points of a plane (starting, end x, end y)
def get_line_intersection_with_plane(line,plane):
    lp1=np.array(line.p1)
    lp2=np.array(line.p2)
    lv = lp2 - lp1
    p1=np.array(plane.p1)
    temp=np.dot(plane.normal, lv)
    if temp==0.0:
        temp=1
    t = np.dot(plane.normal,p1 - lp1) / temp
    return list(lp1 + lv * t)
    
def get_combinations(elements,length):
    return list(itertools.combinations(elements, length))
def square(f):
    return f * f
#returns the normalized normal of the sphere in the point
def sphere_normal(sphere,point):
    temp_normal=[point[0]-sphere.centre[0],point[1]-sphere.centre[1],point[2]-sphere.centre[2]]
    sum_temp=sqrt(temp_normal[0]*temp_normal[0]+temp_normal[1]*temp_normal[1]+temp_normal[2]*temp_normal[2])
    if sum_temp==0:
        return [0,0,0]
    for i in range(3):
        temp_normal[i]=temp_normal[i]/sum_temp
    return temp_normal

def normalize_vector(x,y,z):
    temp=sqrt(x*x+y*y+z*z)
    return x/temp,y/temp,z/temp
def dot_product(p1,p2):
    return p1[0]*p2[0]+p1[1]*p2[1]+p1[2]*p2[2]
    
        
    #returns the point in points which is closest to point
def get_closest_point(points,point):
    minimum=sqrt(square((points[0][0]-point[0])) + square((points[0][1]-point[1])) + square((points[0][1]-point[1])))
    index=0
    for i in range(1,len(points)):
        if not points[i]:continue
        temp=sqrt( square(points[i][0]-point[0]) + square(points[i][1]-point[1]) + square(points[i][2]-point[2]))
        if temp<minimum:
            temp=minimum
            index=i
    return points[index]
def get_distance_between_points(p1,p2):
    return sqrt(square((p1[0]-p2[0])) + square((p1[1]-p2[1])) + square((p1[1]-p2[1])))
def sphere_line_intersection(line, sphere):
    l1=line.p1
    l2=line.p2
    sp=sphere.centre
    r=sphere.radius


    # l1[0],l1[1],l1[2]  P1 coordinates (point of line)
    # l2[0],l2[1],l2[2]  P2 coordinates (point of line)
    # sp[0],sp[1],sp[2], r  P3 coordinates and radius (sphere)
    # x,y,z   intersection coordinates
    #
    # This function returns a pointer array which first index indicates
    # the number of intersection point, followed by coordinate pairs.

    p1 = p2 = None

    a = square(l2[0] - l1[0]) + square(l2[1] - l1[1]) + square(l2[2] - l1[2])
    b = 2.0 * ((l2[0] - l1[0]) * (l1[0] - sp[0]) +
               (l2[1] - l1[1]) * (l1[1] - sp[1]) +
               (l2[2] - l1[2]) * (l1[2] - sp[2]))

    c = (square(sp[0]) + square(sp[1]) + square(sp[2]) + square(l1[0]) +
            square(l1[1]) + square(l1[2]) -
            2.0 * (sp[0] * l1[0] + sp[1] * l1[1] + sp[2] * l1[2]) - square(r))

    i = b * b - 4.0 * a * c

    if i < 0.0:
        pass  # no intersections
    elif i == 0.0:
        # one intersection
        if a==0.0:
            a=0.00001
        mu = -b / (2.0 * a)
        p1 = (l1[0] + mu * (l2[0] - l1[0]),
              l1[1] + mu * (l2[1] - l1[1]),
              l1[2] + mu * (l2[2] - l1[2]),
              )

    elif i > 0.0:
        # first intersection
        mu = (-b + sqrt(i)) / (2.0 * a)
        p1 = (l1[0] + mu * (l2[0] - l1[0]),
              l1[1] + mu * (l2[1] - l1[1]),
              l1[2] + mu * (l2[2] - l1[2]),
              )

        # second intersection
        mu = (-b - sqrt(i)) / (2.0 * a)
        p2 = (l1[0] + mu * (l2[0] - l1[0]),
              l1[1] + mu * (l2[1] - l1[1]),
              l1[2] + mu * (l2[2] - l1[2]),
              )

    return p1, p2
    