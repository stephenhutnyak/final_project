import sys
import pygame

class Settings:
    """Settings for the game"""

    def __init__(self):
        """Initialize"""

        # Window settings
        self.window_width = 800
        self.window_height = 675
        self.bg_color = (2, 2, 2)

        # Player settings
        self.player_speed = 1
