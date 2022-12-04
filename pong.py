# My Pong Game
import sys
import pygame
from settings import Settings
from players import Player1, Player2
from ball import Ball
from button import PlayButton
from power_up import PowerUp
from scoreboard import ScoreboardPlayer1, ScoreboardPlayer2


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
        self.power_up = PowerUp(self)

        self.screen_rect = self.screen.get_rect()

        # Set game status
        self.game_active = False

        # Play button
        self.play_button = PlayButton(self, "Play (Spacebar)")
        self.mouse_pos = pygame.mouse.get_pos()

        # Power ups
        self.power_ups = pygame.sprite.Group()

        # Scoreboard
        self.sb1 = ScoreboardPlayer1(self)
        self.sb2 = ScoreboardPlayer2(self)

        # Music
        self.music = pygame.mixer.Sound("sounds/Music/8-bit.mp3")

    def run_game(self):
        """The main game loop"""

        while True:
            self.music.play()
            self._check_events()

            if self.game_active:
                self.player1.update()
                self.player2.update()
                self.ball.update([self.player1.rect, self.player2.rect])
            self._update_screen()

    def _update_screen(self):
        """Everything updating the screen"""
        self.screen.fill(self.settings.bg_color)
        self.sb1.draw_score()
        self.sb2.draw_score()
        self.player1.blitme()
        self.player2.blitme()
        self.ball.blitme()
        for power_up in self.power_ups:
            pygame.draw.rect(self.screen, self.power_up.color, power_up.rect)

        if not self.game_active:
            self.play_button.draw_button()

        # Show the most recent screen
        pygame.display.flip()

    def _check_events(self):
        """Check for any events that may occur"""
        self.check_point()
        self.check_power_up()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_mouse_events(mouse_pos)

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
        if event.key == pygame.K_SPACE:
            self.game_active = True
        if event.key == pygame.K_p:
            self.create_power_up()
        if event.key == pygame.K_o:
            self.remove_power_up()

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

    def check_mouse_events(self, mouse_pos):
        """Check for any mouse events"""
        self.check_play_button(mouse_pos)

    def check_play_button(self, mouse_pos):
        """Start a new game when the players click Play"""
        if self.play_button.rect.collidepoint(mouse_pos):
            self.game_active = True

            # Prepare the scoreboards
            self.sb1.prep_score()
            self.sb2.prep_score()

    def check_point(self):
        """Check to see if and where the ball leaves the screen"""
        if self.ball.rect.top > self.screen_rect.bottom or \
                self.ball.rect.bottom < self.screen_rect.top:

            # Player 2 point
            if self.ball.rect.top > self.screen_rect.bottom:
                self.sb2.score += 1
                self.sb2.prep_score()

            # Player 1 point
            elif self.ball.rect.bottom < self.screen_rect.top:
                self.sb1.score += 1
                self.sb1.prep_score()

            # Reset Ball
            self.ball.rect.center = self.screen_rect.center
            self.ball.y = float(self.ball.rect.y)
            self.ball.x = float(self.ball.rect.x)

            # Reset Player1
            self.player1.rect.midbottom = self.screen_rect.midbottom
            self.player1.x = float(self.player1.rect.x)
            self.player1.y = float(self.player1.rect.y)

            # Reset Player2
            self.player2.rect.midtop = self.screen_rect.midtop
            self.player2.x = float(self.player2.rect.x)
            self.player2.y = float(self.player2.rect.y)

            # Reset Power Up
            self.end_power_up_ability()

            # Pause the game for a little before starting again
            pygame.time.wait(500)

            self.game_active = False

    def check_power_up(self):
        """Check to see if the ball collided with a power up"""
        for power_up in self.power_ups:
            if self.ball.rect.colliderect(power_up.rect):
                self.remove_power_up()
                if self.settings.ball_direction_y < 0:
                    self.settings.ball_speed_x, self.settings.ball_speed_y = 0.5, 0.75
                    self.settings.player_1_speed = 1
                elif self.settings.ball_direction_y > 0:
                    self.settings.ball_speed_x, self.settings.ball_speed_y = 0.5, 0.75
                    self.settings.player_2_speed = 1

    def end_power_up_ability(self):
        """End the powerups effects"""
        self.settings.ball_speed_x, self.settings.ball_speed_y = 0.25, 0.5
        self.settings.player_1_speed, self.settings.player_2_speed = 0.5, 0.5

    def create_power_up(self):
        """Create a speed power up and add it to the group"""
        new_power_up = PowerUp(self)
        self.power_ups.add(new_power_up)

    def remove_power_up(self):
        """Update the powerups and delete when they collide with the ball"""
        for power_up in self.power_ups.copy():
            self.power_ups.remove(power_up)

# Not ready yet
    def end_game(self):
        """Show the winner after 5 points is reached"""
        font = pygame.font.SysFont("Impact", 100)
        text1 = font.render("Blue Wins!", True, (0, 0, 255))
        text2 = font.render("Red Wins!", True, (255, 0, 0))
        if self.sb1.score == 1:
            pygame.time.delay(1000)

            self.screen.fill((0, 255, 0))
            text1_rect = text1.get_rect()
            text1_rect.center = self.screen_rect.center
            self.screen.blit(text1, text1_rect)

            self.game_active = False


if __name__ == '__main__':
    # Make a game instance and run it
    pong_game = Pong()
    pong_game.run_game()
