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
        return self.ac

class Unit(Point):
    def __init__(self, image):
        super().__init__()
        self.image = image
        
    def setImage(self, image):
        self.image = image
        
    def getImage(self):
        return self.image

class Player(Unit):
    pass

class Enemy(Unit):
    def __init__(self, hp, image):
        super().__init__(image)

class Bullet(Unit):
    def __init__(self, image, owner):
        super().__init__(image)
        self.owner = owner

if __name__ == "__main__":
    a = Enemy(10, pygame.image.load('fireball.png'))
    b = Player(pygame.image.load('plane.png'))
    a.setLocation(1,1)
    a.setSize(1,2)
    print(a.getSize())