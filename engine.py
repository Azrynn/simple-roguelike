import tcod as libtcod
from input.keys import handle_keys

def main():
    screen_width = 80
    screen_height = 50
    player_x = 1
    player_y = 1

    libtcod.console_set_custom_font('data/arial10x10.png', libtcod.FONT_TYPE_GRAYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(screen_width, screen_height, "Roguelike", False)

    main_console = libtcod.console_new(screen_width, screen_height)

    keyboard = libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, keyboard, mouse)

        libtcod.console_set_default_foreground(main_console, libtcod.white)
        libtcod.console_put_char(main_console, player_x, player_y, '@', libtcod.BKGND_NONE)
        libtcod.console_blit(main_console, 0, 0, screen_width, screen_height, 0, 0, 0)
        libtcod.console_flush()

        libtcod.console_put_char(main_console, player_x, player_y, ' ', libtcod.BKGND_NONE)

        # Inputs
        action = handle_keys(keyboard)

        if action.get('move'):
            dx, dy = action.get('move')
            player_x += dx
            player_y += dy   

        if action.get('exit'):
            return True
        
        if action.get('fullscreen'):
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


if __name__ == '__main__':
    main()
