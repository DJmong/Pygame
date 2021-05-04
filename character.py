import pygame

class Point():
    def __init__(self):
        self.xy = [0, 0]
        self.wh = [0, 0]
        self.ac = [0, 0]

    def setSize(self, width, height):
        self.wh = [width, height]
        
    def getSize(self):
        return self.wh
    
    def setLocation(self, x, y):
        self.xy = [x, y]
        
    def getLocation(self):
        return self.xy

    def setAccel(self, ac_x, ac_Y):
        self.ac = [ac_x, ac_y]
        
    def getAccel(self):
        return self.ac_x, self.ac_y    
    
class Key():
    pass

class Unit(Point):
    def __init__(self, hp, Surface):
        self.image = Surface
        
    def setImage(self, Surface):
        self.image = Surface
        
    def getImage(self):
        return self.image

class Player(Unit):
    pass

class Enemy(Unit):
    pass

if __name__ == "__main__":
    a = Enemy(10, pygame.image.load('fireball.png'))
    b = Player(10, pygame.image.load('plane.png'))
    a.setLocation(1,1)
    a.setSize(1,2)
    print(a.getSize())