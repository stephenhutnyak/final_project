# My Pong Game
import sys
import pygame
from settings import Settings
from players import Player1, Player2
from ball import Ball
# from pygame.sprite import Sprite


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
        self.ball = Ball(self)

    def run_game(self):
        """The main game loop"""
        while True:
            self._check_events()
            self.player1.update()
            self.player2.update()
            self.ball.update([self.player1.rect, self.player2.rect])
            self._update_screen()

    def _update_screen(self):
        """Everything updating the screen"""
        self.screen.fill(self.settings.bg_color)
        self.player1.blitme()
        self.player2.blitme()
        self.ball.blitme()

        # Show the most recent screen
        pygame.display.flip()

    def _check_events(self):
        """Check for any events that may occur"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Check for keydown events"""
        if event.key == pygame.K_BACKSPACE:
            sys.exit()
        if event.key == pygame.K_RIGHT:
            self.player1.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.player1.moving_left = True
        if event.key == pygame.K_d:
            self.player2.moving_right = True
        elif event.key == pygame.K_a:
            self.player2.moving_left = True

    def _check_keyup_events(self, event):
        """Check for keyup events"""
        if event.key == pygame.K_RIGHT:
            self.player1.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player1.moving_left = False
        if event.key == pygame.K_d:
            self.player2.moving_right = False
        elif event.key == pygame.K_a:
            self.player2.moving_left = False

if __name__ == '__main__':
    # Make a game instance and run it
    pong_game = Pong()
    pong_game.run_game()
