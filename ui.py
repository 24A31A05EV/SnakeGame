import pygame

from settings import (
    WIDTH,
    HEIGHT,
    BLACK,
    GREEN,
    RED,
    WHITE,
    GRAY
)


class UI:

    def __init__(self):

        self.title_font = pygame.font.SysFont(
            "Arial",
            60,
            bold=True
        )

        self.font = pygame.font.SysFont(
            "Arial",
            30
        )

        self.small_font = pygame.font.SysFont(
            "Arial",
            22
        )

    def draw_text(
        self,
        screen,
        text,
        font,
        color,
        x,
        y
    ):

        surface = font.render(
            text,
            True,
            color
        )

        rectangle = surface.get_rect(
            center=(x, y)
        )

        screen.blit(
            surface,
            rectangle
        )

    def draw_menu(self, screen):

        screen.fill(BLACK)

        self.draw_text(
            screen,
            "SNAKE",
            self.title_font,
            GREEN,
            WIDTH // 2,
            180
        )

        self.draw_text(
            screen,
            "Press SPACE to Start",
            self.font,
            WHITE,
            WIDTH // 2,
            300
        )

        self.draw_text(
            screen,
            "Arrow Keys / WASD to Move",
            self.small_font,
            GRAY,
            WIDTH // 2,
            350
        )

    def draw_game_over(
        self,
        screen,
        score,
        high_score
    ):

        screen.fill(BLACK)

        self.draw_text(
            screen,
            "GAME OVER",
            self.title_font,
            RED,
            WIDTH // 2,
            180
        )

        self.draw_text(
            screen,
            f"Score: {score}",
            self.font,
            WHITE,
            WIDTH // 2,
            280
        )

        self.draw_text(
            screen,
            f"High Score: {high_score}",
            self.font,
            WHITE,
            WIDTH // 2,
            325
        )

        self.draw_text(
            screen,
            "Press R to Restart",
            self.font,
            GREEN,
            WIDTH // 2,
            400
        )

        self.draw_text(
            screen,
            "Press ESC to Menu",
            self.small_font,
            GRAY,
            WIDTH // 2,
            450
        )

    def draw_score(self, screen, score):

        score_text = self.font.render(
            f"Score: {score}",
            True,
            WHITE
        )

        screen.blit(
            score_text,
            (10, 10)
        )