from world.tile import Tile
from world.room import Room
from random import randint

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.init_tiles()
    
    def init_tiles(self):
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]
        return tiles
    
    def is_blocked(self, x, y):
        return self.tiles[x][y].blocked

    def carve_room(self, room):
        # Make all tiles in room passable
        for x in range(room.x1+1, room.x2):
            for y in range(room.y1+1, room.y2):
                self.tiles[x][y].make_passable()
    
    def carve_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2)+1):
            self.tiles[x][y].make_passable()
    
    def carve_v_tunnel(self, x, y1, y2):
        for y in range(min(y1, y2), max(y1, y2)+1):
            self.tiles[x][y].make_passable()

    def generate_rooms(self, max_rooms, room_min_size, room_max_size, map_width, map_height, player):
        # Make a few rooms
        rooms = []
        num_rooms = 0

        while(num_rooms < max_rooms):
            w = randint(room_min_size, room_max_size)
            h = randint(room_min_size, room_max_size)
            x = randint(0, map_width - w - 1)
            y = randint(0, map_height - h - 1)

            new_room = Room(x, y, w, h)
            print("Making room:", x, x+w, y, y+h)
            for other_room in rooms:
                if new_room.intersect(other_room):
                    break
            else:
                self.carve_room(new_room)
                (new_x, new_y) = new_room.center()
                print("With center at:", new_x, new_y)
                if num_rooms == 0:
                    # Is first room
                    player.x = new_x
                    player.y = new_y
                else:
                    # Carve out passage
                    (prev_x, prev_y) = rooms[num_rooms - 1].center()
                    print("Previous room's center was at:", prev_x, prev_y)
                    # flip a coin (random number that is either 0 or 1)
                    if randint(0, 1) == 1:
                        # first move horizontally, then vertically
                        self.carve_h_tunnel(new_x, prev_x, new_y)
                        self.carve_v_tunnel(prev_x, new_y, prev_y)
                    else:
                        # first move vertically, then horizontally
                        self.carve_v_tunnel(new_x, new_y, prev_y)
                        self.carve_h_tunnel(new_x, prev_x, prev_y)
                rooms.append(new_room)
                num_rooms += 1
