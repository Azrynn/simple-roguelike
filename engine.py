import tcod as libtcod
from input.keys import handle_keys
from objects.entity import Entity
from rendering.rendering import draw_scene, clear_entities
from rendering.fov import initialize_fov, compute_fov
from world.map import Map

def main():
    screen_width = 80
    screen_height = 50

    player = Entity(int(screen_width/2), int(screen_height/2), '@', libtcod.white)
    npc = Entity(int(screen_width/2 + 5), int(screen_height/2 + 5), '@', libtcod.red)

    entities = [player, npc]

    map_width = 80
    map_height = 46

    room_max_size = 10
    room_min_size = 6
    max_rooms = 10

    

    map_colors = { 
        'dark_wall' : libtcod.Color(0, 0, 100),
        'dark_ground' : libtcod.Color(50, 50, 150),
        'light_wall' : libtcod.Color(0, 0, 150),
        'light_ground' : libtcod.Color(75, 75, 200),
        }
    game_map = Map(map_width, map_height)
    game_map.generate_rooms(max_rooms, room_min_size, room_max_size, map_height, map_height, player)

    fov_algorithm = 0
    fov_light_walls = True
    fov_radius = 10

    fov_recompute = True
    fov_map = initialize_fov(game_map)

    libtcod.console_set_custom_font('data/arial10x10.png', libtcod.FONT_TYPE_GRAYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(screen_width, screen_height, "Roguelike", False)

    main_console = libtcod.console_new(screen_width, screen_height)

    keyboard = libtcod.Key()
    mouse = libtcod.Mouse()

    

    while not libtcod.console_is_window_closed():
        # Check for keypresses
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, keyboard, mouse)

        #Recompute FOV if needed
        if fov_recompute:
            compute_fov(fov_map, player.x, player.y, fov_radius)
        # Draw entities and map
        draw_scene(main_console, entities, game_map, fov_map, fov_recompute, screen_width, screen_height, map_colors)
        fov_recompute = False

        # Show everything on screen
        libtcod.console_flush()
    
        # Clear entities
        clear_entities(main_console, entities)

        # Handle inputs
        action = handle_keys(keyboard)
        if action.get('move'):
            dx, dy = action.get('move') 
            if not game_map.is_blocked(player.x + dx, player.y + dy):
                player.move(dx, dy)
                fov_recompute = True
        if action.get('exit'):
            return True
        if action.get('fullscreen'):
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


if __name__ == '__main__':
    main()
