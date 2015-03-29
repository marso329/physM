"""
  Author: Martin Söderén
  Email: martin.soderen@gmail.com
  Date: 2015-03-29
  Description: This is a texturecubeclass that inherits from the cubeclass
"""

from objects.cube import *
import physMMath.physMMath as Mmath
import PIL.Image
import numpy as np
class textureCube(cube):
    def __init__(self, length, width, height, texture_file):
        cube.__init__(self,length,width,height,"RED")
        self.texture=self.loadTexture(texture_file)
        self.quads={
        0:(4,5,7,6),
        1:(1,0,3,2),
        2:(3,6,7,2),
        3:(1,5,4,0),
        4:(0,4,6,3),
        5:(2,7,5,1)
        }
        self.normals={
        0:(0,0,1),
        1:(0,0,-1),
        2:(-1,0,0),
        3:(1,0,0),
        4:(0,-1,0),
        5:(0,1,0)
        }
        self.texture_coords={0:(0,0),
                             1:(0,1),
                             2:(1,1),
                             3:(1,0)
                             }
        
    def loadTexture(self,name):
        img = PIL.Image.open(name) 
        img_data = np.array(list(img.getdata()), np.int8)
        texture_id = glGenTextures(1)
        glPixelStorei(GL_UNPACK_ALIGNMENT,1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
        return texture_id
    
    def load_first(self):
        self.update_everything()
        glNewList(self.index, GL_COMPILE)
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [128 / 256.0, 128 / 256.0, 128 / 256.0, 1.0]);
        glMaterialfv(GL_FRONT, GL_SPECULAR, [1, 1, 1, 1]);
        glMaterialfv(GL_FRONT, GL_SHININESS, [128.0]);    
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glBegin(GL_QUADS)
        for i in range(6):
            normal=self.normals[i]
            glNormal(normal[0],normal[1],normal[2])
            for j in range(4):
                tex_coords=self.texture_coords[j]
                glTexCoord2f(tex_coords[0], tex_coords[1])
                glVertex3fv(self.vertices[self.quads[i][j]])
        glEnd()
        glEndList()
        
        #loads all information to the GPU
    def load(self):
        if self.first_load:
            self.load_first()
            self.first_load = False
        else:
            self.update_everything()
            glCallList(self.index)
    
