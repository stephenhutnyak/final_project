import sys
import pygame

class Settings:
    """Settings for the game"""

    def __init__(self):
        """Initialize"""

        # Window settings
        self.window_width = 655
        self.window_height = 710
        self.bg_color = (2, 2, 2)

        # Player settings
        self.player_speed = 0.5

        # Ball settings
        self.ball_speed_y = 0.5
        self.ball_speed_x = 0.5
        self.ball_direction_y = 1
        self.ball_direction_x = 1

