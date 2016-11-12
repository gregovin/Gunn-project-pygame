import pygame
import math
def atan3(y, x):
   if x==0 and y==0:
      return 0
   elif x==0 and y>0:
      return math.pi/2
   elif x==0:
      return -math.pi/2
   else:
      return math.atan2(y, x)
player = [200, 200, 0, 0, 0]
class Enimy:
   def update(self):
      self.pos[0] = self.pos[0] + self.vel[0]
      self.pos[1] = self.pos[1] + self.vel[0]
      
   def __init__(self, poses, vels):
      self.pos = poses
      self.vel = vels
      self.rot = atan3(vels[1],vels[0])
pygame.init
   
