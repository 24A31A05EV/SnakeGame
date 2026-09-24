import pygame

from settings import (
    WIDTH,
    HEIGHT,
    BLACK,
    FPS,
    MAX_FPS,
    CELL_SIZE,
    GRID_COLOR
)

from snake import Snake
from food import Food
from ui import UI


class Game:

    def __init__(self):

        self.screen = pygame.display.set_mode(
            (WIDTH, HEIGHT)
        )

        pygame.display.set_caption("Snake Game")

        self.clock = pygame.time.Clock()

        self.snake = Snake()

        self.food = Food()

        self.ui = UI()

        self.score = 0

        self.high_score = 0

        self.state = "menu"

        self.paused = False

        self.reset()

    def reset(self):

        self.snake.reset()

        self.score = 0

        self.paused = False

        self.food.spawn(self.snake.body)

    def handle_events(self):

        for event in pygame.event.get():

            # Close window
            if event.type == pygame.QUIT:

                return False

            if event.type == pygame.KEYDOWN:

                # MENU
                if self.state == "menu":

                    if event.key == pygame.K_SPACE:

                        self.reset()

                        self.state = "playing"

                # PLAYING
                elif self.state == "playing":

                    # Pause / Resume
                    if event.key == pygame.K_p:

                        self.paused = not self.paused

                    # Movement
                    elif not self.paused:

                        self.handle_movement(event.key)

                # GAME OVER
                elif self.state == "game_over":

                    if event.key == pygame.K_r:

                        self.reset()

                        self.state = "playing"

                    elif event.key == pygame.K_ESCAPE:

                        self.state = "menu"

        return True

    def handle_movement(self, key):

        if key in (
            pygame.K_UP,
            pygame.K_w
        ):

            self.snake.change_direction(
                [0, -CELL_SIZE]
            )

        elif key in (
            pygame.K_DOWN,
            pygame.K_s
        ):

            self.snake.change_direction(
                [0, CELL_SIZE]
            )

        elif key in (
            pygame.K_LEFT,
            pygame.K_a
        ):

            self.snake.change_direction(
                [-CELL_SIZE, 0]
            )

        elif key in (
            pygame.K_RIGHT,
            pygame.K_d
        ):

            self.snake.change_direction(
                [CELL_SIZE, 0]
            )

    def update(self):

        # Don't update when not playing
        if self.state != "playing":

            return

        # Don't move while paused
        if self.paused:

            return

        new_head = self.snake.move()

        # Food collision
        if new_head == self.food.position:

            self.score += 1

            if self.score > self.high_score:

                self.high_score = self.score

            self.food.spawn(
                self.snake.body
            )

        else:

            self.snake.remove_tail()

        # Wall collision
        hit_wall = (
            new_head[0] < 0
            or new_head[0] >= WIDTH
            or new_head[1] < 0
            or new_head[1] >= HEIGHT
        )

        # Self collision
        hit_self = self.snake.check_self_collision()

        if hit_wall or hit_self:

            self.state = "game_over"

    def draw(self):

        # MENU
        if self.state == "menu":

            self.ui.draw_menu(
                self.screen
            )

        # PLAYING
        elif self.state == "playing":

            self.screen.fill(BLACK)

            # Draw vertical grid lines
            for x in range(
                0,
                WIDTH,
                CELL_SIZE
            ):

                pygame.draw.line(
                    self.screen,
                    GRID_COLOR,
                    (x, 0),
                    (x, HEIGHT)
                )

            # Draw horizontal grid lines
            for y in range(
                0,
                HEIGHT,
                CELL_SIZE
            ):

                pygame.draw.line(
                    self.screen,
                    GRID_COLOR,
                    (0, y),
                    (WIDTH, y)
                )

            # Draw snake
            self.snake.draw(
                self.screen
            )

            # Draw food
            self.food.draw(
                self.screen
            )

            # Draw score
            self.ui.draw_score(
                self.screen,
                self.score
            )

            # Draw pause screen
            if self.paused:

                self.ui.draw_text(
                    self.screen,
                    "PAUSED",
                    self.ui.title_font,
                    (255, 255, 0),
                    WIDTH // 2,
                    HEIGHT // 2
                )

                self.ui.draw_text(
                    self.screen,
                    "Press P to Resume",
                    self.ui.font,
                    (255, 255, 255),
                    WIDTH // 2,
                    HEIGHT // 2 + 70
                )

        # GAME OVER
        elif self.state == "game_over":

            self.ui.draw_game_over(
                self.screen,
                self.score,
                self.high_score
            )

        pygame.display.flip()

    def run(self):

        running = True

        while running:

            running = self.handle_events()

            self.update()

            self.draw()

            # Increase speed as score increases
            speed = min(
                MAX_FPS,
                FPS + self.score // 3
            )

            self.clock.tick(speed)