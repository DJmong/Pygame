import pygame
import random
import character as ch
import bgm
from time import sleep

Color = (255, 255, 255)
width = 740
height = 345
background_width = width

bat_width = 110
aircraft_width = 90
aircraft_height = 55
    
def drawObject(obj, x, y):
    global gamepad
    gamepad.blit(obj, (x, y))
    
def runGame():
    global gamepad, user, clock, background1, background2
    global bat, fires

    bullet_xy = []
    
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
                elif event.key == pygame.K_LCTRL:
                    bullet_x = x + aircraft_width
                    bullet_y = y + aircraft_height/2
                    bullet_xy.append([bullet_x, bullet_y])
                
                elif event.key == pygame.K_SPACE:
                    sleep(5)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        

        gamepad.fill(Color)
        
        background1_x -= speed
        background2_x -= speed

        if background1_x <= -background_width:
            background1_x = background_width
        
        if background2_x <= -background_width:
           background2_x = background_width
        
        drawObject(background1, background1_x, 0)
        drawObject(background2, background2_x, 0)

       

   
        y += y_change

        if y < 0:
            y = 0
        elif y > height - aircraft_height:
            y = height - aircraft_height
        
        drawObject(user.getImage(), x, y)
        

        if fire == None:
            fire_x -= 30

        else:
            fire_x -= 15
            
        if fire_x <= 0:
            fire_x = width
            fire_y = random.randrange(0, height)
            random.shuffle(fires)
            fire = fires[0]

        if fire != None:
            drawObject(fire, fire_x, fire_y)
   
        bat_x -= 7
        if bat_x <= 0:
            bat_x = width
            bat_y = random.randrange(0, height)
 
        drawObject(bat.getImage(), bat_x, bat_y)
            

        if len(bullet_xy) != 0:
            for i, bxy in enumerate(bullet_xy):
                bxy[0] += 15
                bullet_xy[i][0] = bxy[0]
                if bxy[0] >= width:
                    bullet_xy.remove(bxy)
        
        if len(bullet_xy) != 0:
            for bx, by in bullet_xy:
                drawObject(bullet, bx, by)
                
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

def initGame():
    global gamepad, user, clock, background1, background2
    global bat, fires, bullet
    
    fires = []
    pygame.init()
    gamepad = pygame.display.set_mode((width, height))
    
    user = ch.Player(100, pygame.image.load('plane.png'))
    pygame.display.set_caption("Test")
    background1 = pygame.image.load('background.png')
    background2 = background1.copy()
 
    bat = ch.Enemy(100, pygame.image.load('bat.png'))
    fires.append(pygame.image.load('fireball.png'))
    fires.append(pygame.image.load('fireball2.png'))  
    
    bullet = pygame.image.load('bullet.png')

    for i in range(5):
        fires.append(None)
         
    clock = pygame.time.Clock()
    runGame()

if __name__ == "__main__":
    initGame()
