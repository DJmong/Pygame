import random

from source import character as ch
from source import engine as eg
from source import resolution as res


class Bat(ch.Enemy):
    def __init__(self):
        super().__init__(10, 'graphic/bat.png')
        self.setSize(100, 60)
        self.setLocation(res.width, random.randrange(0, res.height - self.wh[1]))
        self.setAccel(-6, 0)
        
class SuperBat(ch.Enemy):
     def __init__(self):
        super().__init__(80, 'graphic/bat.png')
        self.setSize(300, 240)
        self.setLocation(res.width, random.randrange(0, res.height - self.wh[1]))
        self.setAccel(-1, 0)