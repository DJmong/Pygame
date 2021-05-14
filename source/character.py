import pygame


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
        
    def getRect(self):      
        return pygame.Rect(self.xy[0], self.xy[1]. self.wh[0], self.wh[1])

class Unit(Point):
    def __init__(self, image):
        super().__init__()
        self.setImage(image)
        self.wh = [0, 0]
    
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
    def key_ins(self, key):
        pass
    
    def Attack(self):
        atk = Bullet('graphic/bullet.png', self)
        atk.setSize(20,5)
        atk.setMaxAccel(250, 0)
        
        Bullet_x = self.xy[0] + self.wh[0]
        Bullet_y = self.xy[1] + self.wh[1] / 2
        atk.setLocation(Bullet_x, Bullet_y)
        
        atk.setAccel(15, 0)
        return atk
class Enemy(Unit):
    def __init__(self, hp, image):
        super().__init__(image)
        self.hp = hp
        
    def getHp(self):
        return self.hp
    
    def __add__(self, hp):
        self.hp += hp
    
    def __sub__(self, hp):
        self.hp -= hp
        
    
        

class Bullet(Unit):
    def __init__(self, image, owner):
        super().__init__(image)
        self.setOwn(owner)
        
    def setOwn(self, owner):
        self.owner = owner
    
    def getOwn(self):
        return self.owner
        
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