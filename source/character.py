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

    def setAccel(self, ac_x, ac_y):
        self.ac = [ac_x, ac_y]
        
    def getAccel(self):
        return self.ac

    def move(self):
        x = 0
        y = 1
        self.xy[x] += self.ac[x]
        self.xy[y] += self.ac[y]

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
        self.setOwn(owner)
        
    def setOwn(self, owner):
        self.owner = owner
        
    def isOwner(self, obj):
        if self.owner == obj:
            return True
        else:
            return False

if __name__ == "__main__":
    a = Enemy(10, pygame.image.load('graphic/fireball.png'))
    a.setLocation(1,2)
    a.setAccel(2, 1)
    a.move()
    print(a.getLocation())