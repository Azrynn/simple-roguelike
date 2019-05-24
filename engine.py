import tcod as libtcod
from input.keys import handle_keys
from objects.entity import Entity
from rendering.rendering import draw_entities, clear_entities

def main():
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 46

    libtcod.console_set_custom_font('data/arial10x10.png', libtcod.FONT_TYPE_GRAYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(screen_width, screen_height, "Roguelike", False)

    main_console = libtcod.console_new(screen_width, screen_height)

    keyboard = libtcod.Key()
    mouse = libtcod.Mouse()

    player = Entity(int(screen_width/2), int(screen_height/2), '@', libtcod.white)
    npc = Entity(int(screen_width/2 + 5), int(screen_height/2 + 5), '@', libtcod.red)

    entities = [player, npc]

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, keyboard, mouse)

        # Draw entities
        draw_entities(main_console, entities, screen_width, screen_height)
        
        # Show everything on screen
        libtcod.console_flush()
    
        # Clear entities
        clear_entities(main_console, entities)

        # Handle inputs
        action = handle_keys(keyboard)

        if action.get('move'):
            dx, dy = action.get('move') 

        if action.get('exit'):
            return True
        
        if action.get('fullscreen'):
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


if __name__ == '__main__':
    main()
