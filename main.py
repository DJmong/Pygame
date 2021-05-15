import pygame
import random
from source import bgm
from source import character as ch
from source import engine as eg
from time import sleep

Color = (255, 255, 255)
RED = (255, 0, 0)
width = 1280
height = 480
background_width = width

img_user = 'graphic/backup.png'
img_enemy = 'graphic/bat.png'
img_bg = 'graphic/background.png'

bat_width = 100
bat_height = 60

fireball1_width = 140
fireball1_height = 60
fireball2_width = 86
fireball2_height = 60

aircraft_width = 80
aircraft_height = 40
    
def textObj(text, font):
    textSurface = font.render(text, True, RED)
    return textSurface, textSurface.get_rect()

def dispMessage(text):
    global gamepad
    
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = textObj(text, largeText)
    TextRect.center = ((width / 2), (height / 2))
    gamepad.blit(TextSurf, TextRect)
    pygame.display.update()
    sleep(2)
    runGame()
    
def crash():
    global gamepad
    dispMessage('Crashed!')
    
def drawObject(obj, x, y):
    global gamepad
    gamepad.blit(obj, (x, y))
    
def runGame():
    global gamepad, user, clock, background1, background2
    global bat, fires, boom

    eg.add_unit(bat)
    eg.add_unit(user)

    bullet_list = []
    
    batDeath = False
    boom_count = 0

    user.setLocation(width * 0.05, height * 0.8)

    background1_x = 0
    background2_x = background_width
    speed = 2
    
    bat.setLocation(width, random.randrange(0, height))
    
    fire_x = width
    fire_y = random.randrange(0, height)
    random.shuffle(fires)
    fire = fires[0]
    
    bgm.setBgmVolume(0.4)
    bgm.playBgm('sound/music.mp3')
    
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                accel_x, accel_y = user.getAccel()
                if event.key == pygame.K_UP:
                    accel_y += -6
                if event.key == pygame.K_DOWN:
                    accel_y += 6
                if event.key == pygame.K_LEFT:
                    accel_x += -6
                if event.key == pygame.K_RIGHT:
                    accel_x += 6

                if accel_x > 25:
                    accel_x = 25
                elif accel_x < -25:
                    accel_x = -25

                if accel_y > 25:
                    accel_y = 25
                elif accel_y < -25:
                    accel_y = -25

                user.setAccel(accel_x, accel_y)
                
                if event.key == pygame.K_LCTRL:
                    bullet = user.Attack()
                    eg.add_unit(bullet)
                    bullet_list.append(bullet)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    accel_x, accel_y = user.getAccel()
                    user.setAccel(accel_x, 0)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    accel_x, accel_y = user.getAccel()
                    user.setAccel(0, accel_y)
                    
        x, y = user.getLocation()        

        gamepad.fill(Color)
        
        background1_x -= speed
        background2_x -= speed

        if background1_x <= -background_width:
            background1_x = background_width
        
        if background2_x <= -background_width:
            background2_x = background_width
        
        drawObject(background1, background1_x, 0)
        drawObject(background2, background2_x, 0)


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

        bat.setAccel(-7, 0)
        bat_x, bat_y = bat.getLocation()
        if bat_x <= 0:
            bat.setLocation(width, random.randrange(0, height - bat_height))

        bat_x, bat_y = bat.getLocation()
        #bullet check for bat
        if len(bullet_list) != 0:
            for bullet in bullet_list:
                isShotBat = eg.chk_Collision(bullet, bat)
                if isShotBat == True:
                    bullet_list.remove(bullet)
                    batDeath = True
                    continue
                b_x, b_y = bullet.getLocation()
                
                if b_y > height or b_y < 0 or b_x > width or b_x < 0:
                    bullet_list.remove(bullet)


        #crash check for 
        if x + aircraft_width > bat_x:
            if (y > bat_y and y < bat_y + bat_height) or\
            (y + aircraft_height > bat_y and y + aircraft_height < bat_y + bat_height):
                crash()
        
        #fire crash check
        if fire[1] != None:
            if fire[0] == 0:
                fireball_width = fireball1_width
                fireball_height = fireball1_height
            elif fire[0] == 1:
                fireball_width = fireball2_width
                fireball_height = fireball2_height
            
            if x + aircraft_width > fire_x:
                if (y > fire_y and y < fire_y + fireball_height) or\
                (y + aircraft_height > fire_y and y + aircraft_height < fire_y + fireball_height):
                    crash()
        
        bat_x, bat_y = bat.getLocation()

        if not batDeath:
            drawObject(bat.getImage(), bat_x, bat_y)
        else:
            if boom_count == 0:
                bgm.playSfx('sound/sfx.mp3')    
            boom_count += 1
            drawObject(boom, bat_x, bat_y)
            
            if boom_count > 6:
                bat.setLocation(width, random.randrange(0, height - bat_height))
                batDeath = False
                boom_count = 0
                            
        if len(bullet_list) != 0:
            for bullet in bullet_list:
                bx, by = bullet.getLocation()
                drawObject(bullet.getImage(), bx, by)
        
        if fire[1] != None:
            drawObject(fire[1], fire_x, fire_y)

        eg.move_unit()
        
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

def initGame():
    global gamepad, user, clock, background1, background2
    global bat, fires, bullet, boom
    
    fires = []
    pygame.init()
    gamepad = pygame.display.set_mode((width, height))
    
    user = ch.Player(img_user)
    user.setSize(aircraft_width, aircraft_height)
    
    pygame.display.set_caption("Test")
    background1 = pygame.image.load(img_bg)
    background1 = pygame.transform.scale(background1, (width, height))
    background2 = background1.copy()
 
    bat = ch.Enemy(100, img_enemy)
    bat.setSize(bat_width, bat_height)
    
    fires.append((0, pygame.image.load('graphic/fireball.png')))
    fires.append((0, pygame.image.load('graphic/fireball2.png')))  
    boom = pygame.image.load('graphic/boom.png')
 
    
    for i in range(3):
        fires.append((i+2, None))
         
    clock = pygame.time.Clock()
    runGame()

if __name__ == "__main__":
    initGame()
