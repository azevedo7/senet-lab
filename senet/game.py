import pygame
from .constants import WHITE, BLACK, BLUE, SQ_SIZE, HEIGHT, WIDTH, PADDING
from .board import Board
from .sticks import Stick
from .button import Button


class Game:
    def __init__(self, screen):
        self.move = pygame.mixer.Sound('audio\move.wav')
        self.over = False
        self.winner = None  # BLACK or WHITE
        self.selected = None
        self.board = Board(screen)
        self.board.create_board()
        self.sticks = Stick()
        self.valid_moves = {}
        self.turn = WHITE
        self.play_again = False
        self.screen = screen

        # Buttons
        # button_font = pygame.font.Font("Senet_font-Regular.ttf", 34)
        # button_image = pygame.transform.rotozoom(pygame.image.load('images\menu\img_none.png'), 0, 0.3)
        # self.exit_button = Button(button_image, pos=(WIDTH / 2, HEIGHT * 0.80), text_input='BACK',
        #                           font=button_font, base_color="black", hovering_color="white")

    def update(self):
        self.board.print_board(self.screen)
        self.sticks.draw_sticks(self.screen)
        self.draw_valid_moves()
        # self.exit_button.update(self.screen)
        self.valid_moves = self.board.calc_valid_moves(self.sticks.calc_mov(), self.turn)
        self.print_turn()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        else:
            piece = self.board.get_piece(row, col)
            if piece is None:
                return False
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                return True
        return False

    def _move(self, row, col):
        if self.valid_moves == {}:
            self.change_turn()
            self.sticks.throw()
            return False
        if self.valid_moves.get((self.selected.row, self.selected.col)) is not None:
            if self.selected and self.valid_moves[(self.selected.row, self.selected.col)] == (row, col):
                self.move.play()
                self.board.move(self.selected, row, col)
                self.selected = None

                if (row, col) == (2, 10):  # Check if it's out of the board:
                    self.board.remove_piece(row, col, self.turn)
                    self.check_win()

                self.play_again = self.sticks.play_again()
                if not self.play_again:
                    self.change_turn()
                self.sticks.throw()
                self.board.special_houses(row, col)
            else:
                return False
        else:
            return False
        return True

    def change_turn(self):
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE

    def draw_valid_moves(self):
        if self.selected:
            cord = self.valid_moves.get((self.selected.row, self.selected.col))
            if cord:
                row, col = cord
                pygame.draw.circle(self.screen, "green",
                                   [col * SQ_SIZE + SQ_SIZE // 2 + PADDING, row * SQ_SIZE + SQ_SIZE // 2 + PADDING], 5)

    def print_turn(self):
        font = pygame.font.Font("Newathenaunicode-EP3l.ttf", 32)

        if self.turn == BLACK:
            color = "Black"
        else:
            color = "White"
        text = font.render(f'Turn: {color}', True, WHITE)

        text_rect = text.get_rect(center=(WIDTH * 0.7, HEIGHT * 0.71))
        self.screen.blit(text, text_rect)

    def check_win(self):
        if self.board.white_left == 0:
            self.over = True
            self.winner = WHITE
        elif self.board.black_left == 0:
            self.over = True
            self.winner = BLACK

