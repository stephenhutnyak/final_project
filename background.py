import pygame


class Background:
    """Class to manage the background of the screen"""

    def __init__(self):
        """Initialize the background elements"""
        # 0 is grey, 1 is black
        self.grid = [[0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                     [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                     [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
                     [0, 1, 1, 1, 0, 0, 1, 1, 0, 0],
                     [0, 1, 1, 0, 1, 0, 1, 1, 0, 0],
                     [0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                     [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
                     [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     ]


        # Define our tiles
        self.grey = pygame.image.load("images/Tiles/Tiles (Grayscale)/tile_0014.png")
        self.black = pygame.image.load("images/Tiles/Tiles (Grayscale)/tile_0013.png")

        self.tiles = [self.grey, self.black]

        # Find dimensions of tile rect
        self.tile_rect = self.grey.get_rect()

    def draw_background(self):
        """Draw the tiles to the screen"""
        bg = pygame.Surface(self.bg_size)
        # Draw each tile
        for r, grid_list in enumerate(self.grid):
            for c, grid_element in enumerate(grid_list):
                bg.blit(self.tiles[grid_element], (c*self.TILE_SIZE, r*self.TILE_SIZE))
        return bg
