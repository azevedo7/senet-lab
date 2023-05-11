import pygame
from .constants import LIGHT, DARK, ROWS, COLS, SQ_SIZE

class Board:
    def __init__(self):
        self.board = [["w1", "b1", "w2", "b2", "w3", "b3", "w4", "b4", "w5", "b5"],
                      ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
                      ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"]]
        self.selected_piece = None
        self.black_left = 5
        self.white_left = 5

    def draw_squares(self, win):
        win.fill(LIGHT)
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2:
                    pygame.draw.rect(win, DARK, (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                