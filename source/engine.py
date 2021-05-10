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

def chk_crash():
    pass

if __name__ == '__main__':
    pass