import pygame


class Player1:
    """This is our bottom player"""

    def __init__(self, pong_game):
        """Initialize the player and set its starting position"""
        self.screen = pong_game.screen
        self.settings = pong_game.settings
        self.screen_rect = pong_game.screen.get_rect()

        # Load the player image
        self.image = pygame.image.load("images/PNG/Blue/characterBlue (1).png")
        self.image = pygame.transform.scale(self.image, self.settings.player_1_size)
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()

        # Start the player at the bottom center of the screen,
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the player's position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

        # Build rects for the sides of the players
        self.right_rect = pygame.Rect(0, 0, 40, 50)

    def blitme(self):
        """Draw the player at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the x value of the player"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_1_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.player_1_speed

        # Update rect object from self.x
        self.rect.x = self.x


class Player2:
    """This is our top player"""

    def __init__(self, pong_game):
        """Initialize top player"""
        self.screen = pong_game.screen
        self.settings = pong_game.settings
        self.screen_rect = pong_game.screen.get_rect()

        # Load the player image
        self.image = pygame.image.load("images/PNG/Red/characterRed (1).png")
        self.image = pygame.transform.scale(self.image, self.settings.player_2_size)
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()

        # Start the player at the top center of the screen
        self.rect.midtop = self.screen_rect.midtop

        # Store a decimal value for the player's position
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the player at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_2_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.player_2_speed

        # Update rect object form self.x
        self.rect.x = self.x
