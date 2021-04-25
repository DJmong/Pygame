import pygame

Color = (255, 255, 255)
width = 800
height = 600

def airplane(x, y):
    global gamepad, aircraft
    gamepad.blit(aircraft, (x, y))

def runGame():
    global gamepad, clock

    x = width * 0.05
    y = height * 0.8
    y_change = 0

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        
        y += y_change

        gamepad.fill(Color)
        airplane(x, y)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

def initGame():
    global gamepad, aircraft, clock

    pygame.init()
    gamepad = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Test")
    aircraft = pygame.image.load('plane.png')

    clock = pygame.time.Clock()
    runGame()

if __name__ == "__main__":
    initGame()
