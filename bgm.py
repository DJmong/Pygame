import pygame

def playmusic(soundfile):
    pygame.mixer.init()
    pygame.mixer.music.load(soundfile)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)

def stopmusic():
    pygame.mixer.music.stop()

def test():
    while(1):
        pass

if __name__ == '__main__':
    pygame.init()
    playmusic('music.mp3')
    test()