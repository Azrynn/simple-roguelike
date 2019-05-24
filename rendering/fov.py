import tcod as libtcod

def initialize_fov(map):
    fov_map = libtcod.map_new(map.width, map.height)
    for y in range(map.height):
        for x in range(map.width):
            libtcod.map_set_properties(fov_map, x, y, not map.tiles[x][y].blocks_sight, not map.tiles[x][y].blocked)
    return fov_map

def compute_fov(fov_map, x, y, radius, light_walls=True, algorithm=0):
    libtcod.map_compute_fov(fov_map, x, y, radius, light_walls, algorithm)