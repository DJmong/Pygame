import pygame

def init():
    pygame.mixer.init()

def playBgm(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)

def setBgmVolume(volume):
    pygame.mixer.music.set_volume(volume)

def stopBgm():
    pygame.mixer.music.stop()

def playSfx(file):
    pygame.mixer.init()
    Sound = pygame.mixer.Sound(file)
    pygame.mixer.Sound.play(Sound)

def test():
    while(1):
        pass

if __name__ == '__main__':
    pygame.init()
    setBgmVolume(0.3)
    playBgm('music.mp3')
    playSfx('sfx.mp3')
    test()