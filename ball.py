import pygame
from players import Player1, Player2
from settings import Settings


class Ball:
    """A class for our ball"""

    def __init__(self, pong_game):
        """Initialize the ball's stuff"""
        self.player1 = Player1(pong_game)
        self.player2 = Player2(pong_game)
        self.screen = pong_game.screen
        self.settings = pong_game.settings
        self.screen_rect = pong_game.screen.get_rect()

        # Load the ball image
        self.image = pygame.image.load("images/PNG/Equipment/ball_generic1.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()

        # Place the ball in the center of the screen
        self.rect.center = self.screen_rect.center

        # Decimal value for the ball's position
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the ball at its current location"""
        self.screen.blit(self.image, self.rect)

    def check_collision(self):
        """Check to see if the ball needs to bounce"""
        player1_rect = self.player1.rect
        player2_rect = self.player2.rect

        if self.rect.colliderect(player1_rect) or self.rect.colliderect(player2_rect):
            return True

    def update(self):
        """Update the position of the ball"""
        collide1 = self.rect.colliderect(self.player1)
        collide2 = self.rect.colliderect(self.player2)
        if self.check_collision():
            self.settings.ball_direction *= -1

        self.y += (self.settings.ball_speed *
                   self.settings.ball_direction)
        self.rect.y = self.y
