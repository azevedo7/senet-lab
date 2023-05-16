import pygame
from .constants import LIGHT, DARK, ROWS, COLS, SQ_SIZE, WHITE, BLACK, WIDTH
from .pieces import Piece

class Board:    
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.black_left = 5
        self.white_left = 5

    def draw_squares(self, screen):
        screen.fill(LIGHT)
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2:
                    pygame.draw.rect(screen, DARK, (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                match row, col:
                    case 2,6:
                        image = pygame.image.load('images\specialCases\img_16.png')
                        image = pygame.transform.scale(image, (SQ_SIZE,SQ_SIZE))
                        image_rect = image.get_rect(bottomleft=(5*SQ_SIZE, 2*SQ_SIZE))
                        screen.blit(image,image_rect)



                

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row == 0:
                    if col % 2 == 0:
                        self.board[row].append(Piece(row, col, WHITE))
                    else:
                        self.board[row].append(Piece(row, col, BLACK))
                else:
                    self.board[row].append(0)

    def select_piece(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        row = mouse_y // SQ_SIZE
        col = mouse_x // SQ_SIZE
        if row <= ROWS-1 and col <= COLS-1:
            if self.board[row][col] != 0:
                self.board[row][col].select()

    def print_board(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(screen)

        pygame.draw.line(screen, DARK, (0, 3 * SQ_SIZE), (WIDTH, 3 * SQ_SIZE), 2)
