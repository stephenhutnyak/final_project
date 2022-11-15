import pygame
from pygame.sprite import Sprite

pygame.init()

TILE_SIZE = 64
WINDOW_WIDTH = 10 * TILE_SIZE
WINDOW_HEIGHT = 8 * TILE_SIZE

# 0 is grass, 1 is mud, 2 is sand
grid = [
    [0, 0, 1, 1, 2, 2, 1, 1, 0, 0, ],
    [0, 0, 1, 1, 2, 2, 1, 1, 0, 0, ],
    [0, 0, 1, 1, 2, 2, 1, 1, 0, 0, ],
    [0, 0, 1, 1, 2, 2, 1, 1, 0, 0, ],
    [0, 0, 1, 1, 2, 2, 1, 1, 0, 0, ],
    [0, 0, 1, 1, 2, 2, 1, 1, 0, 0, ],
    [0, 0, 1, 1, 2, 2, 1, 1, 0, 0, ],
    [0, 0, 1, 1, 2, 2, 1, 1, 0, 0, ],
]

# define images for background
grass = pygame.image.load("images/Environment/grass.png")
mud = pygame.image.load("images/Environment/mud.png")
sand = pygame.image.load("images/Environment/sand.png")

# grab the dimensions of our tile rectangle
tile_rect = grass.get_rect()

# draw screen with background
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

width_loc = 0
height_loc = 0

# draw each tile onto background
for row in grid:
    for i in row:
        # blit the correct tile onto background
        screen.blit(soils[i], (width_loc,height_loc))
        width_loc += width_loc += TILE_SIZE
    height_loc += TILE_SIZE
    width_loc = 0

pygame.display.flip()
