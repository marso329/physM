import numpy as np
import itertools

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
        
#takes in three points and calculates
def calc_plane(v1,v2,v3):
    x=[v1[0],v2[0],v3[0]]
    y=[v1[1],v2[1],v3[1]]
    z=[v1[2],v2[2],v3[2]]
    a = np.column_stack((x, y, z))
    return list(np.linalg.lstsq(a, np.ones_like(x))[0])

# takes a vector (tuple of 2 points, each with a tuple of 3 coordinates)
# and a tuple of three points of a plane (starting, end x, end y)
def get_line_intersection_with_plane(line,plane):
    lp1=np.array(line.p1)
    lp2=np.array(line.p2)
    lv = lp2 - lp1
    p1=np.array(plane.p1)
    t = np.dot(plane.normal,p1 - lp1) / np.dot(plane.normal, lv)
    return lp1 + lv * t
def get_combinations(elements,length):
    return list(itertools.combinations(elements, length))

    