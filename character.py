class Unit():
    def __init__(self, hp):
        self.hp = hp
    
    def __init__(self, hp, x, y):
        self.hp = hp
        self.x = x
        self.y = y

class Player(Unit):
    pass

class Enemy(Unit):
    pass