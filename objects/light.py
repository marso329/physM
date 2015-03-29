"""
  Author: Martin Söderén
  Email: martin.soderen@gmail.com
  Date: 2015-03-29
  Description: This is a lightclass that inherits from the ObjectSuperClass
"""

from objects.objectSuperClass import *
import physMMath.physMMath as Mmath

class light(objectSuperClass):

    def __init__(self, x,y,z):
        objectSuperClass.__init__(self)
        self.light=con.lights[var.number_of_light]
        var.number_of_light+=1
        self.position=(x,y,z,1)
        self.ambient = [0.0, 0.0, 0.0, 1.0]
        self.diffuse=[1, 1, 1, 1]
        self.specular=[1, 1, 1, 1]
        self.direction=[0,0,-1]
        self.light_angle=40
        self.exponent=2
        self.enabled=True
    
    def turn_light_off(self):
        glDisable(self.light)
    
    def turn_light_on(self):
        glEnable(self.light)
        
    def load_first(self):
        glLightfv(self.light, GL_AMBIENT, self.ambient)
        glLightfv(self.light, GL_DIFFUSE, self.diffuse)
        glLightfv(self.light, GL_SPECULAR, self.specular)
        glLightfv(self.light, GL_POSITION, self.position)
        glEnable(self.light)
        
    def load(self):
        if self.first_load:
            self.load_first()
            self.first_load=False
        glLightfv(self.light, GL_POSITION, self.position)
        glLightf(self.light, GL_SPOT_CUTOFF, self.light_angle)
        glLightfv(self.light, GL_SPOT_DIRECTION, self.direction)
        glLightf(self.light, GL_SPOT_EXPONENT, self.exponent)
        
