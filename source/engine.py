import pygame

list_unit = list()

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
    Rect_a = unit_a.getRect()
    Rect_b = unit_b.getRect()
    return Rect_a.colliderect(Rect_b)
    

if __name__ == '__main__':
    pass