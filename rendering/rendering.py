import tcod as libtcod
from objects.entity import Entity

def draw_entity(console, entity):
    libtcod.console_set_default_foreground(console, entity.color)
    libtcod.console_put_char(console, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)

def clear_entity(console, entity):
        libtcod.console_put_char(console, entity.x, entity.y, ' ', libtcod.BKGND_NONE)

def draw_entities(console, entities, screen_width, screen_height):
    for entity in entities:
        draw_entity(console, entity)
    libtcod.console_blit(console, 0, 0, screen_width, screen_height, 0, 0, 0)

def clear_entities(console, entities):
    for entity in entities:
        clear_entity(console, entity)