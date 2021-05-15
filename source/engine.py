import pygame

list_unit = list()

def drawObject(obj, x, y):
    global gamepad
    gamepad.blit(obj, (x, y))

def move_unit():
    global list_unit
    for unit in list_unit:
        unit.move()

def add_unit(unit):
    global list_unit
    list_unit.append(unit)

def del_unit(unit):
    global list_unit
    if unit in list_unit:
        list_unit.remove(unit)

def chk_Collision(unit_a, unit_b):
    x_a, y_a = unit_a.getLocation()
    w_a, h_a = unit_a.getSize()
    
    x_b, y_b = unit_b.getLocation()
    w_b, h_b = unit_b.getSize()
    
    if x_a + w_a > x_b:
        if (y_a > y_b and y_a < y_b + h_b) or\
        (y_a + h_a > y_b and y_a + h_a < y_b + h_b):
            return True
    return False
    
    

if __name__ == '__main__':
    pass