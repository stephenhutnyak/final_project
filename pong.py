# My Pong Game
import sys
import pygame
from settings import Settings
from players import Player1, Player2
from pygame.sprite import Sprite


# Main game class
class Pong:
    """Overall class to manage the game"""

    def __init__(self):
        """Initialize"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.window_width,
                                               self.settings.window_height))
        pygame.display.set_caption("Pong")

        self.player1 = Player1(self)
        self.player2 = Player2(self)

    def run_game(self):
        """The main game loop"""
        while True:
            self._check_events()
            self.screen.fill(self.settings.bg_color)
            self.player1.blitme()
            self.player2.blitme()

            # Show the most recent screen
            pygame.display.flip()

    def _check_events(self):
        """Check for any events that may occur"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()


if __name__ == '__main__':
    # Make a game instance and run it
    pong_game = Pong()
    pong_game.run_game()
