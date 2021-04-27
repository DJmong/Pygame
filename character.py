import pygame

class Unit():
    def __init__(self, hp):
        self.hp = hp
    
    def __init__(self, hp, x, y):
        self.__init__(hp)
        self.x = x
        self.y = y
        
    def __init__(self, hp, x, y, Surface):
        self.__init__(hp, x, y)
        image = Surface
        
class Player(Unit):
    pass

class Enemy(Unit):
    pass