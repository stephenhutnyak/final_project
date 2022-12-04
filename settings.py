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
        self.player_1_speed = 0.5
        self.player_2_speed = 0.5
        self.player_1_size = (40, 100)
        self.player_2_size = (40, 100)

        # Ball settings
        self.ball_speed_y = 0.5
        self.ball_speed_x = 0.25
        self.ball_direction_y = 1
        self.ball_direction_x = 1

        # Powerup settings
        self.power_up_width = 50
        self.power_up_height = 50

        # Sounds
        self.player_bounce_sound = pygame.mixer.Sound("sounds/Impact/impactGeneric_light_000.ogg")
        self.wall_bounce_sound = pygame.mixer.Sound("sounds/Impact/impactGeneric_light_004.ogg")
        self.point_sound = pygame.mixer.Sound("sounds/Voice/you_lose.ogg")

# Helping Hand

    # Me
        # 11/17 Helped Thomas Bui with centering image.rect on another image.rect
        # 11/29 Helped Thomas figure out how to rotate cue stick around cue ball
        # 11/29 Helped Thomas center cue stick rect
        # 12/1 Helped Thomas with changing the screen upon victory
        # 12/1 Helped Thomas play sound

    # Thomas
        # 12/1 Helped me track score
        # 12/1 Helped me display score on screen
        # 12/1 Helped me show game over screen
        # 12/1 Helped me change sound
        # 12/1 Helped me change font
