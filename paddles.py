import pygame


class Paddle1:
    """This is our bottom paddle"""

    def __init__(self, pong_game):
        """Initialize the paddle and set its starting position"""
        self.screen = pong_game.screen
        self.screen_rect = pong_game.screen.get_rect()

        # Load the paddle image
        self.image = pygame.image.load("images/PNG/Equipment/racket_wood.png")
        self.rect = self.image.get_rect()

        # Start the paddle at the bottom center of the screen,
        # Raised a couple of pixels
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the paddle at its current location"""
        self.screen.blit(self.image, self.rect)
