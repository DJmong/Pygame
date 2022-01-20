import pygame
from source import resolution as res

list_draw = list()
list_unit = list()
list_enemy = list()
list_bullet = list()
list_enemy_bullet = list()

def start_game():
    global gamepad
    pygame.init()
    gamepad = pygame.display.set_mode((res.width, res.height))

def drawObject(obj, location):
    gamepad.blit(obj, location)

def bullet_collision(bullet_list, unit_list):
    for bullet in bullet_list:
        for unit in unit_list:
            chk_collision(bullet, unit)

def move_unit():
    global list_unit
    for unit in list_unit:
        unit.move()

def chk_user_collision(user):
    for enemy in list_enemy:
        if chk_collision(user, enemy):
            return True
    
    for bullet in list_enemy_bullet:
        if chk_collision(user, bullet):
            return True
        
    return False

def add_enemy(enemy):
    global list_enemy
    list_enemy.append(enemy)

def del_enemy(enemy):
    global list_enemy
    if enemy in list_unit:
        list_enemy.remove(enemy)

def add_unit(unit):
    global list_unit
    list_unit.append(unit)

def del_unit(unit):
    global list_unit
    if unit in list_unit:
        list_unit.remove(unit)

def chk_collision(unit_a, unit_b):
    x_a, y_a = unit_a.getLocation()
    w_a, h_a = unit_a.getSize()
    
    x_b, y_b = unit_b.getLocation()
    w_b, h_b = unit_b.getSize()
    
    if x_a + w_a > x_b and x_a < x_b + w_b:
        if y_a + h_a > y_b and y_a < y_b + h_b:
            return True
    return False

def add_draw(object):
    list_draw.append(object)

def del_draw(object):
    if object in list_draw:    
        list_draw.remove(object)
    
if __name__ == '__main__':
    pass