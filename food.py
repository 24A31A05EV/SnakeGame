import random
import pygame

from settings import WIDTH, HEIGHT, CELL_SIZE, RED


class Food:

    def __init__(self):
        self.position = [0, 0]

    def spawn(self, snake_body):

        while True:

            x = random.randrange(
                0,
                WIDTH,
                CELL_SIZE
            )

            y = random.randrange(
                0,
                HEIGHT,
                CELL_SIZE
            )

            position = [x, y]

            if position not in snake_body:
                self.position = position
                break

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            RED,
            (
                self.position[0],
                self.position[1],
                CELL_SIZE,
                CELL_SIZE
            )
        )