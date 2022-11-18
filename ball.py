import pygame
from settings import Settings


class Ball:
    """A class for our ball"""

    def __init__(self, pong_game):
        """Initialize the ball's stuff"""
        self.screen = pong_game.screen
        self.settings = pong_game.settings
        self.screen_rect = pong_game.screen.get_rect()
        self.move_x = False

        # Load the ball image
        self.image = pygame.image.load("images/PNG/Equipment/ball_generic1.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()

        # Place the ball in the center of the screen
        self.rect.center = self.screen_rect.center

        # Decimal value for the ball's position
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the ball at its current location"""
        self.screen.blit(self.image, self.rect)

    def check_collision_player(self, player_rect_list):
        """Check to see if the ball needs to bounce"""
        if self.rect.colliderect(player_rect_list[0]) or \
                self.rect.colliderect(player_rect_list[1]):
            return True
        else:
            return False

    def check_collision_wall(self):
        """Check if there's a collision with the wall"""
        if self.rect.right >= self.screen_rect.right or \
                self.rect.left <= self.screen_rect.left:
            return True

    def update(self, player_rect_list):
        """Update the position of the ball"""
        if self.check_collision_player(player_rect_list):
            self.settings.ball_direction_y *= -1
            self.move_x = True

        if self.check_collision_wall():
            self.settings.ball_direction_x *= -1

        self.update_x()
        self.update_y()

    def update_x(self):
        """Function to move the ball left and right"""
        if self.move_x:
            self.x += (self.settings.ball_speed_x *
                       self.settings.ball_direction_x)
            self.rect.x = self.x

    def update_y(self):
        """Function to move the ball up and down"""
        self.y += (self.settings.ball_speed_y *
                   self.settings.ball_direction_y)
        self.rect.y = self.y
