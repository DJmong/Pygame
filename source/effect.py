import pygame
from source import character as ch
from source import engine as eg

class Boom(ch.Sfx):
    def __init__(self, xy, ac):
        super().__init__(xy, [30, 25], ac)
        self.setMaxCount(15)
        
        
if __name__ == '__main__':
    eg.start_game()
    while 1:
        pass