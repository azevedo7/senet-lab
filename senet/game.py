import pygame
from .constants import WHITE, BLACK
from .board import Board
from .sticks import Stick


class Game:
    def __init__(self, screen):
        self.selected = None
        self.board = Board()
        self.board.create_board()
        self.sticks = Stick()
        self.valid_moves = []
        self.turn = WHITE
        self.play_again = False
        self.screen = screen

    def update(self):
        self.board.print_board(self.screen)

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        else:
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.calc_valid_moves(piece)
                return True
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.selected = None
            self.play_again = self.sticks.play_again()
            if not self.play_again:
                self.change_turn()
            self.sticks.throw()
        else:
            return False
        return True

    def change_turn(self):
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE

    def calc_valid_moves(self, piece):
        self.valid_moves = []
        houses = self.sticks.calc_mov()
        
        house_sum = piece.col + houses
        house_sub = piece.col - houses

        if piece.row % 2 == 0:
            if house_sum < 10:
                self.valid_moves.append((piece.row, piece.col + houses))
            elif house_sum >= 10:
                self.valid_moves.append((piece.row + 1, 9 - (house_sum - 10)))
        elif piece.row == 1:
            if house_sub >= 0:
                self.valid_moves.append((piece.row, house_sub))
            if house_sub < 0:
                self.valid_moves.append((piece.row + 1, abs(house_sub) - 1))
