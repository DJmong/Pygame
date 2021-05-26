import pygame
import os
import random
from source import resolution as res
from source import engine as eg

class Point():
    def __init__(self):
        self.xy = [0, 0]
        self.ac = [0, 0]
        self.max_ac = [0, 0]
        
    def setLocation(self, x, y):
        self.xy = [x, y]
        
    def getLocation(self):
        return self.xy

    def setAccel(self, ac_x, ac_y):
        self.ac = [ac_x, ac_y]
        
    def getAccel(self):
        return self.ac

    def setMaxAccel(self, x, y):
        self.max_ac = [x, y]

    def getMaxAccel(self):
        return self.max_ac

    def move(self):
        self.xy[0] += self.ac[0]
        self.xy[1] += self.ac[1]        

class Unit(Point):
    def __init__(self, image):
        super().__init__()
        self.setImage(image)
        self.wh = [0, 0]
        eg.add_unit(self)
    
    def __del__(self):
        eg.del_unit(self)
    
    def setImage(self, image):
        self.image = pygame.image.load(image)
        
    def getImage(self):
        return self.image  
    
    def setSize(self, width, height):
        self.wh = [width, height]
        self.image = pygame.transform.scale(self.image, (width, height))
        
    def getSize(self):
        return self.wh

class Player(Unit):
    def __init__(self, image):
        super().__init__(image)
        
    def Attack(self):
        atk = Bullet('graphic/bullet.png', self, 3)
        atk.setSize(20,5)
        atk.setMaxAccel(250, 0)
        
        Bullet_x = self.xy[0] + self.wh[0]
        Bullet_y = self.xy[1] + self.wh[1] / 2
        atk.setLocation(Bullet_x, Bullet_y)
        
        atk.setAccel(15, 0)
        return atk
    
    def move(self):
        self.xy[0] += self.ac[0]
        self.xy[1] += self.ac[1]
        
        if self.xy[0] + self.wh[0] >= res.width:
            self.xy[0] = res.width - self.wh[0]
            
        elif self.xy[0] <= 0:
            self.xy[0] = 0
            
        if self.xy[1] + self.wh[1] >= res.height:
            self.xy[1] = res.height - self.wh[1]
        
        elif self.xy[1] <= 0:
            self.xy[1] = 0 
    
class Enemy(Unit):
    def __init__(self, hp, image):
        super().__init__(image)
        self.hp = hp
        eg.add_enemy(self)
        
    def __del__(self):
        super().__del__()
        eg.del_enemy(self)
        
    def getHp(self):
        return self.hp
    
    def take_dmg(self, hp):
        self.hp -= hp
        
    def is_dead(self):
        if self.hp <= 0:
            return True
        else:
            return False
        
class Bullet(Unit):
    def __init__(self, image, owner, dmg):
        super().__init__(image)
        self.setOwn(owner)
        self.setDamage(dmg)
        
    def setDamage(self, dmg):
        self.damage = dmg
        
    def getDamage(self):
        return self.damage
        
    def setOwn(self, owner):
        self.owner = owner
    
    def getOwn(self):
        return self.owner
        
    def isOwner(self, obj):
        if self.owner == obj:
            return True
        else:
            return False

class Sfx(Unit):
    def __init__(self, image, xy, wh, ac):
        super().__init__(image)
        self.setLocation(xy[0], xy[1])
        self.setSize(wh[0], wh[1])
        self.setAccel(ac[0], ac[1])
    
        
    
if __name__ == "__main__":
    pass