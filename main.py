import pygame
import random
import character as ch

Color = (255, 255, 255)
width = 740
height = 345
background_width = width


    
def drawObject(obj, x, y):
    global gamepad
    gamepad.blit(obj, (x, y))
    
def runGame():
    global gamepad, aircraft, clock, background1, background2
    global bat, fires

    obj
    x = width * 0.05
    y = height * 0.8
    y_change = 0

    background1_x = 0
    background2_x = background_width
    speed = 2
    
    bat_x = width
    bat_y = random.randrange(0, height)
    
    fire_x = width
    fire_y = random.randrange(0, height)
    random.shuffle(fires)
    fire = fires[0]
    
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
        
        bat_x -= 7
        if bat_x <= 0:
            bat_x = width
            bat_y = random.randrange(0, height)
        
        if fire == None:
            fire_x -= 30
        else:
            fire_x -= 15
            
        if fire_x <= 0:
            fire_x = width
            fire_y = random.randrange(0, height)
            random.shuffle(fires)
            fire = fires[0]
            
        if background1_x <= -background_width:
            background1_x = background_width
        
        
        if background2_x <= -background_width:
           background2_x = background_width
        
        
        drawObject(background1, background1_x, 0)
        drawObject(background2, background2_x, 0)
        drawObject(bat, bat_x, bat_y)
        
        if fire != None:
            drawObject(fire, fire_x, fire_y)
        drawObject(aircraft, x, y)
        
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

def initGame():
    global gamepad, aircraft, clock, background1, background2
    global bat, fires
    
    fires = []
    
    pygame.init()
    gamepad = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Test")
    aircraft = pygame.image.load('plane.png')
    background1 = pygame.image.load('background.png')
    background2 = background1.copy()
 
    bat = pygame.image.load('bat.png')
    fires.append(pygame.image.load('fireball.png'))
    fires.append(pygame.image.load('fireball2.png'))  
    
    for i in range(5):
        fires.append(None)
         
    clock = pygame.time.Clock()
    runGame()

if __name__ == "__main__":
    a = ch.Enemy(10,1,1, pygame.image.load('fireball.png'))
    b = ch.Unit(10,1,1)
    a = pygame.image.load('fireball.png')
    print(type(a))
    
    # initGame()
