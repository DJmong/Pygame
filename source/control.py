from source import engine as eg
from source import character as ch
from source import enemy as en

def create_enemy(key, name):
    if(name == "Bat"):
        unit = en.Bat()
        
    eg.add_enemy(unit)
    eg.add_unit(unit)
    eg.add_draw(unit)

def remove_enemy(unit):
    eg.del_enemy(unit)
    eg.del_unit(unit)
    eg.del_draw(unit)
    del(unit)