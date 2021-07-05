import pygame
from source import character as ch
from source import engine as eg
from source import bgm as bgm
class Boom(ch.Sfx):
    def __init__(self, xy, ac):
        super().__init__(xy, [30, 25], ac)
        self.setMaxCount(15)
        bgm.playSfx('sound/sfx.mp3')  
        
        
if __name__ == '__main__':
    eg.start_game()
    while 1:
        pass