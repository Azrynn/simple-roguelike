class Tile:
    """
    Generic tile object
    """
    def __init__(self, blocked, blocks_sight=None):
        self.blocked = blocked
        if blocks_sight == None:
            blocks_sight = blocked
        self.blocks_sight = blocks_sight
    
    def make_passable(self):
        self.blocked = self.blocks_sight = False
    