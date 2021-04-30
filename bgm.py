import pygame

class Bgm():
    def __init__(self):
        pygame.mixer.init()
        self.setVolume(0.5)
        self.file = ''

    def __init__(self, file):
        pygame.mixer.init()
        self.setVolume(0.5)
        self.setMusic(file)

    def setMusic(self, file):
        self.file = file

    def play(self):
        pygame.mixer.music.load(self.file)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(self.volume)

    def setVolume(self, volume):
        self.volume = volume

    def stopmusic(self):
        pygame.mixer.music.stop()

class Sfx():
    def __init__(self):
        pygame.mixer.init()
        self.file = ''

    def setMusic(self, file):
        self.file = file

    def play(self, file):
        Sound = pygame.mixer.Sound('sfx.mp3')
        pygame.mixer.Sound.play(Sound)

    def stopmusic(self):
        pygame.mixer.Sound.stop()

def test():
    while(1):
        pass

if __name__ == '__main__':
    pygame.init()
    b = Bgm('music.mp3')
    c = Sfx()
    b.play()
    c.play('sfx.mp3')
    test()