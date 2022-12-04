import pygame


class ScoreboardPlayer1:
    """A class to manage the score for player 1"""

    def __init__(self, pong_game):
        self.screen = pong_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = pong_game.settings
        self.score = 0

        # Font settings for scoring info
        self.color = (255, 255, 255)
        self.font = pygame.font.SysFont("Impact", 100)

        # Prepare the initial score image
        self.prep_score()

    def prep_score(self):
        """Prepares the score"""
        score_string = str(self.score)
        self.score_image = self.font.render(score_string, True, self.color, self.settings.bg_color)

        # Display the score at the bottom right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.bottom = self.screen_rect.bottom - 20

    def draw_score(self):
        """Draw the score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)


class ScoreboardPlayer2:
    """A class to manage the score for player 2"""
    def __init__(self, pong_game):
        self.screen = pong_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = pong_game.settings
        self.score = 0

        # Font settings for scoring info
        self.color = (255, 255, 255)
        self.font = pygame.font.SysFont("Impact", 100)

        # Prepare the initial score image
        self.prep_score()

    def prep_score(self):
        """Prepares the score"""
        score_string = str(self.score)
        self.score_image = self.font.render(score_string, True, self.color, self.settings.bg_color)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = self.screen_rect.top + 20

    def draw_score(self):
        """Draw the score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)