from loader.setup import *
from objects import cube, objectFile, sphere, cylinder
import random

colors=["YELLOW","BLUE","RED","WHITE","GREEN"]
for i in range(20):
    temp=sphere.sphere(1.0,colors[random.randint(0,4)])
    temp.change_position(random.randint(-5,5),0,random.randint(-5,5))
    temp.change_velocity(random.randint(-5,5),0,random.randint(-5,5))
    temp.mass=random.randint(0,5)
    temp.enable_gravity()




glutMainLoop()
