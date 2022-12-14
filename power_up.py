import pygame
from pygame.sprite import Sprite
import random


class PowerUp(Sprite):
    """A class to build our power ups"""

    def __init__(self, pong_game):
        """Initialize attributes"""
        super().__init__()
        self.screen = pong_game.screen
        self.settings = pong_game.settings
        self.color = (255, 0, 0)

        # Create the powerup rect at (0, 0) and then set position
        self.rect = pygame.Rect(0, 0, self.settings.power_up_width,
                                self.settings.power_up_height)
        self.rect.center = (random.randint(0, self.settings.window_width),
                            random.randint(300, self.settings.window_height - 300))

        # Store the position as a decimal value
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
