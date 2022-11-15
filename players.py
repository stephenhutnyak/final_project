import pygame


class Player1:
    """This is our bottom player"""

    def __init__(self, pong_game):
        """Initialize the player and set its starting position"""
        self.screen1 = pong_game.screen
        self.settings = pong_game.settings
        self.screen_rect1 = pong_game.screen.get_rect()

        # Load the player image
        self.image1 = pygame.image.load("images/PNG/Blue/characterBlue (1).png")
        self.image1 = pygame.transform.scale(self.image1, (40, 100))
        self.image1 = pygame.transform.rotate(self.image1, 90)
        self.rect1 = self.image1.get_rect()

        # Start the player at the bottom center of the screen,
        self.rect1.midbottom = self.screen_rect1.midbottom

    def blitme(self):
        """Draw the paddle at its current location"""
        self.screen1.blit(self.image1, self.rect1)


class Player2:
    """This is our top player"""

    def __init__(self, pong_game):
        """Initialize top player"""
        self.screen2 = pong_game.screen
        self.screen_rect2 = pong_game.screen.get_rect()

        # Load the player image
        self.image2 = pygame.image.load("images/PNG/Red/characterRed (1).png")
        self.image2 = pygame.transform.scale(self.image2, (40, 100))
        self.image2 = pygame.transform.rotate(self.image2, -90)
        self.rect2 = self.image2.get_rect()

        # Start the player at the bottom center of the screen,
        self.rect2.midtop = self.screen_rect2.midtop

    def blitme(self):
        """Draw the paddle at its current location"""
        self.screen2.blit(self.image2, self.rect2)