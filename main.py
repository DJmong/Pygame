import pygame
import random
import copy
from source import bgm
from source import character as ch
from source import engine as eg
from source import resolution as res
from source import enemy
from time import sleep

Color = (255, 255, 255)
RED = (255, 0, 0)

res.width = 1280
res.height = 480

img_user = 'graphic/backup.png'
img_bg = 'graphic/background.png'


aircraft_width = 80
aircraft_height = 40
    
def textObj(text, font):
    textSurface = font.render(text, True, RED)
    return textSurface, textSurface.get_rect()

def dispMessage(text):

    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = textObj(text, largeText)
    TextRect.center = ((res.width / 2), (res.height / 2))
    eg.gamepad.blit(TextSurf, TextRect)
    pygame.display.update()
    sleep(2)
    runGame()
    
def crash():
    dispMessage('Crashed!')
    

    
def runGame():
    global user, clock, background1, background2
    global bat, boom
    
    bullet_list = []
    batDeath = False
    boom_count = 0
    
    user.setLocation(res.width * 0.05, res.height * 0.8)
    
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
                    bullet_list.append(bullet)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    accel_x, accel_y = user.getAccel()
                    user.setAccel(accel_x, 0)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    accel_x, accel_y = user.getAccel()
                    user.setAccel(0, accel_y)

        eg.gamepad.fill(Color)
        
        background1_x, background1_y = background1.getLocation()
        background_width, background_height = background1.getSize()
        background2_x, background2_y = background2.getLocation()
        background2_width, background2_height = background1.getSize()

        if background1_x <= -background_width:
            background1_x = background_width
        
        if background2_x <= -background2_width:
            background2_x = background2_width
        
        eg.drawObject(background1.getImage(), background1.getLocation())
        eg.drawObject(background2.getImage(), background2.getLocation())

        background1.setLocation(background1_x, background1_y)
        background2.setLocation(background2_x, background2_y)
        
        eg.drawObject(user.getImage(), user.getLocation())


        bat_x, bat_y = bat.getLocation()
        bat_w, bat_h = bat.getSize()
        if bat_x <= 0:
            bat.setLocation(res.width, random.randrange(0, res.height - bat_h))

        bat_x, bat_y = bat.getLocation()
        #bullet check for bat
        if len(bullet_list) != 0:
            for bullet in bullet_list:
                isShotBat = eg.chk_collision(bullet, bat)
                if isShotBat == True:
                    bat.take_dmg(bullet.getDamage())
                    bullet_list.remove(bullet)
                    if bat.is_dead():
                        batDeath = True
                    continue
                b_x, b_y = bullet.getLocation()
                
                if b_y > res.height or b_y < 0 or b_x > res.width or b_x < 0:
                    bullet_list.remove(bullet)
                    continue

        #crash check
        if eg.chk_user_collision(user):
            crash()
        

      
        bat_x, bat_y = bat.getLocation()
        bat_w, bat_h = bat.getSize();
        if not batDeath:
            eg.drawObject(bat.getImage(), bat.getLocation())
            
        else:
            if boom_count == 0:
                bgm.playSfx('sound/sfx.mp3')    
            boom_count += 1
            eg.drawObject(boom, (bat_x, bat_y))
            
            if boom_count > 6:
                del(bat)
                bat = enemy.Bat()
                batDeath = False
                boom_count = 0
                            
        if len(bullet_list) != 0:
            for bullet in bullet_list:
                eg.drawObject(bullet.getImage(), bullet.getLocation())
        

        eg.move_unit()
        
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

def initGame():
    global user, clock, background1, background2
    global bat, bullet, boom
    
    eg.start_game()
    user = ch.Player(img_user)
    user.setSize(aircraft_width, aircraft_height)
    
    pygame.display.set_caption("Test")

    background1 = ch.Unit(img_bg)
    background1.setLocation(0,0)
    background1.setSize(res.width, res.height)
    background1.setAccel(-2, 0)
    
    background2 = ch.Unit(img_bg)
    background2.setLocation(res.width,0)
    background2.setSize(res.width, res.height)
    background2.setAccel(-2, 0)

 
    bat = enemy.Bat()
    
    boom = pygame.image.load('graphic/boom.png')
 
    

    clock = pygame.time.Clock()
    runGame()

if __name__ == "__main__":
    initGame()
