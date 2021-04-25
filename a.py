import pygame

Color = (255, 255, 255)
width = 740
height = 345
background_width = width

def back(background, x, y):
    global gamepad
    gamepad.blit(background, (x,y))

def airplane(x, y):
    global gamepad, aircraft
    gamepad.blit(aircraft, (x, y))

def runGame():
    global gamepad, clock, background1, background2

    x = width * 0.05
    y = height * 0.8
    y_change = 0

    background1_x = 0
    background2_x = background_width
    speed = 2
    
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
        
        background1_x -= speed
        background2_x -= speed
        
        if background1_x <= -background_width:
            background1_x = background_width
        
        
        if background2_x <= -background_width:
           background2_x = background_width
        
        
        back(background1, background1_x, 0)
        back(background2, background2_x, 0)
        
        airplane(x, y)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

def initGame():
    global gamepad, aircraft, clock, background1, background2

    pygame.init()
    gamepad = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Test")
    aircraft = pygame.image.load('plane.png')
    background1 = pygame.image.load('background.png')
    background2 = background1.copy()
    
    clock = pygame.time.Clock()
    runGame()

if __name__ == "__main__":
    initGame()
