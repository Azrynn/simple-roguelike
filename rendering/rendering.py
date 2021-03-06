import tcod as libtcod
from objects.entity import Entity

def draw_entity(console, entity, fov_map):
    if libtcod.map_is_in_fov(fov_map, entity.x, entity.y):
        libtcod.console_set_default_foreground(console, entity.color)
        libtcod.console_put_char(console, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)

def clear_entity(console, entity):
        libtcod.console_put_char(console, entity.x, entity.y, ' ', libtcod.BKGND_NONE)

def draw_scene(console, entities, map, fov_map, fov_recompute, screen_width, screen_height, colors):
    # Draw map
    if fov_recompute:
        for y in range(map.height):
            for x in range(map.width):
                visible = libtcod.map_is_in_fov(fov_map, x, y)
                wall = map.tiles[x][y].blocks_sight
                if visible:
                    if wall:
                        libtcod.console_set_char_background(console, x, y, colors.get('light_wall'), libtcod.BKGND_SET)
                    else:
                        libtcod.console_set_char_background(console, x, y, colors.get('light_ground'), libtcod.BKGND_SET)
                else:
                    if wall:
                        libtcod.console_set_char_background(console, x, y, colors.get('dark_wall'), libtcod.BKGND_SET)
                    else:
                        libtcod.console_set_char_background(console, x, y, colors.get('dark_ground'), libtcod.BKGND_SET)
    # Draw entities
    for entity in entities:
        draw_entity(console, entity, fov_map)
    libtcod.console_blit(console, 0, 0, screen_width, screen_height, 0, 0, 0)

def clear_entities(console, entities):
    for entity in entities:
        clear_entity(console, entity)