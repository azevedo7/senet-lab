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
        # Row ranges from 0 to 2
        for row in range(ROWS):
            # Col ranges from 0 to 9
            for col in range(COLS):
                if (row + col) % 2:
                    pygame.draw.rect(screen, DARK, (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                match row, col:
                    case 1, 5:
                        image = pygame.image.load('images\specialCases\img_16.png')
                        image = pygame.transform.scale(image, (SQ_SIZE, SQ_SIZE))
                        image_rect = image.get_rect(bottomleft=(5 * SQ_SIZE, 2 * SQ_SIZE))
                        screen.blit(image, image_rect)
                    case 2, 5:
                        image = pygame.image.load('images\specialCases\img_26.png')
                        image = pygame.transform.scale(image, (SQ_SIZE, SQ_SIZE))
                        image_rect = image.get_rect(bottomleft=(5 * SQ_SIZE, 3 * SQ_SIZE))
                        screen.blit(image, image_rect)
                    case 2, 6:
                        image = pygame.image.load('images\specialCases\img_27.png')
                        image = pygame.transform.scale(image, (SQ_SIZE, SQ_SIZE))
                        image_rect = image.get_rect(bottomleft=(6 * SQ_SIZE, 3 * SQ_SIZE))
                        screen.blit(image, image_rect)
                    case 2, 7:
                        image = pygame.image.load('images\specialCases\img_28.png')
                        image = pygame.transform.scale(image, (SQ_SIZE, SQ_SIZE))
                        image_rect = image.get_rect(bottomleft=(7 * SQ_SIZE, 3 * SQ_SIZE))
                        screen.blit(image, image_rect)
                    case 2, 8:
                        image = pygame.image.load('images\specialCases\img_29.png')
                        image = pygame.transform.scale(image, (SQ_SIZE, SQ_SIZE))
                        image_rect = image.get_rect(bottomleft=(8 * SQ_SIZE, 3 * SQ_SIZE))
                        screen.blit(image, image_rect)
                    case 2, 9:
                        image = pygame.image.load('images\specialCases\img_30.png')
                        image = pygame.transform.scale(image, (SQ_SIZE, SQ_SIZE))
                        image_rect = image.get_rect(bottomleft=(9 * SQ_SIZE, 3 * SQ_SIZE))
                        screen.blit(image, image_rect)

    def move(self, piece, row, col):
        second_piece = self.get_piece(row, col)
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        if second_piece:
            second_piece.move(piece.row, piece.col)
        piece.move(row, col)

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

    # def select_piece(self):
    #     mouse_x, mouse_y = pygame.mouse.get_pos()
    #
    #     row = mouse_y // SQ_SIZE
    #     col = mouse_x // SQ_SIZE
    #     if row <= ROWS - 1 and col <= COLS - 1:
    #         if self.board[row][col] != 0:
    #             self.board[row][col].select()

    def get_piece(self, row, col):
        return self.board[row][col]

    def print_board(self, screen):
        self.draw_squares(screen)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(screen)

        pygame.draw.line(screen, DARK, (0, 3 * SQ_SIZE), (WIDTH, 3 * SQ_SIZE), 2)
