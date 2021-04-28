import pygame

class Key():
    pass

class Unit():
    def __init__(self, hp, Surface):
        self.hp = hp
        self.x = 0
        self.y = 0
        self.image = Surface
        
    def getImage(self):
        return self.image
    
    def setLocation(self, x, y):
        self.x = x
        self.y = y
        
    def getLocation(self):
        return self.x, self.y
    
class Player(Unit):
    pass

class Enemy(Unit):
    pass

if __name__ == "__main__":
    a = Enemy(10, pygame.image.load('fireball.png'))
    b = Player(10, pygame.image.load('plane.png'))
    a.setLocation(1,1)
    x, y = a.getLocation()