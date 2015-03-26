from objects.objectSuperClass import *
import physMMath.physMMath as Mmath
class sphere(objectSuperClass):

    def __init__(self,radius,color):
        assert(isinstance(radius, (int,float)) and radius>0.0)
        objectSuperClass.__init__(self)
        self.check_color(color)
        self.quadratic = gluNewQuadric()
        gluQuadricNormals(self.quadratic, GLU_SMOOTH)  
        gluQuadricTexture(self.quadratic, GL_TRUE)
        self.first_load=True
        self.radius=radius
        self.index = glGenLists(1)
        self.max_distance_from_centre=radius
        self.collision_enabled=True
        self.calculation_sphere=None
    #checks so point is inside this object, use  unproject if its a point on the edges
    def check_point(self,point):
        marginal=var.marginal_for_checking_boundary_checking
        temp_point=Mmath.calculate_unprojection_point(self, self.position[0], self.position[1], self.position[2])
        temp=Mmath.get_distance_between_points(temp_point, point)
        temp=temp<=self.radius
        print(temp)
        return temp
    def get_normal(self,point):
        return Mmath.sphere_normal(self.calculation_sphere, point)
    def get_boundary_point(self,object_in_world):
        line_between_objects=self.get_line_between_objects(object_in_world)
        self.calculation_sphere=Mmath.sphere(tuple(self.position),self.radius)
        solutions=Mmath.sphere_line_intersection(line_between_objects, self.calculation_sphere)
        return Mmath.get_closest_point(solutions, tuple(object_in_world.position))
    def load_first(self):
        self.update_everything()
        glNewList(self.index, GL_COMPILE)
        if not self.transparency_enabled:
            glColor3f(self.color[0],self.color[1],self.color[2])
        else:
            glColor4f(self.color[0],self.color[1],self.color[2],self.transparency)
            
        gluSphere(self.quadratic,self.radius,32,32)
        glEndList()
    def load(self):
        if self.first_load:
            self.load_first()
            self.first_load=False
        else:
            self.update_everything()
            glCallList(self.index)
        