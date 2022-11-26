import sys
import pygame
import random

class Settings:
    """Settings for the game"""

    def __init__(self):
        """Initialize"""

        # Window settings
        self.tile_size = 12
        self.window_width = 700
        self.window_height = 700
        self.bg_color = (15, 15, 15)

        # Player settings
        self.player_speed = 0.5

        # Ball settings
        self.ball_speed_y = 0.5
        self.ball_speed_x = 0.25
        self.ball_direction_y = 1
        self.ball_direction_x = random.randint(-1, 1)

        # Sounds
        self.player_bounce_sound = pygame.mixer.Sound("sounds/Impact/impactGeneric_light_000.ogg")
        self.wall_bounce_sound = pygame.mixer.Sound("sounds/Impact/impactGeneric_light_004.ogg")

# Helping Hand
    # 11/17 Helped Thomas Bui with centering image.rect on another image.rect
