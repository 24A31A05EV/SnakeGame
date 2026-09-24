import pygame

from settings import CELL_SIZE, GREEN, DARK_GREEN


class Snake:

    def __init__(self):
        self.reset()

    def reset(self):
        self.body = [
            [300, 300],
            [280, 300],
            [260, 300]
        ]

        self.direction = [CELL_SIZE, 0]

    def move(self):
        new_head = [
            self.body[0][0] + self.direction[0],
            self.body[0][1] + self.direction[1]
        ]

        self.body.insert(0, new_head)

        return new_head

    def remove_tail(self):
        self.body.pop()

    def grow(self):
        pass

    def change_direction(self, new_direction):

        opposite = [
            -self.direction[0],
            -self.direction[1]
        ]

        if new_direction != opposite:
            self.direction = new_direction

    def check_self_collision(self):

        return self.body[0] in self.body[1:]

    def draw(self, screen):

        for index, segment in enumerate(self.body):

            if index == 0:
                color = DARK_GREEN
            else:
                color = GREEN

            pygame.draw.rect(
                screen,
                color,
                (
                    segment[0],
                    segment[1],
                    CELL_SIZE,
                    CELL_SIZE
                )
            )