import pygame.draw
from .constants import SQ_SIZE


class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQ_SIZE * self.col + SQ_SIZE // 2
        self.y = SQ_SIZE * self.row + SQ_SIZE // 2

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), SQ_SIZE/3)
