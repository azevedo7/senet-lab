import pygame.draw
from .constants import SQ_SIZE


class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.selected = False

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQ_SIZE * self.col + SQ_SIZE // 2
        self.y = SQ_SIZE * self.row + SQ_SIZE // 2

    def draw(self, screen):
        if self.selected:
            pygame.draw.rect(screen, "green", (self.col * SQ_SIZE, self.row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        pygame.draw.circle(screen, self.color, (self.x, self.y), SQ_SIZE/3)

    def select(self):
        self.selected = True

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

