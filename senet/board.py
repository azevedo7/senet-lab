import pygame
from .constants import *
from .pieces import Piece


class Board:
    def __init__(self, screen):
        self.board = []
        self.valid_moves = {}
        self.selected_piece = None
        self.black_left = 5
        self.white_left = 5
        self.screen = screen

    def draw_squares(self, screen):
        # Row ranges from 0 to 2
        for row in range(ROWS):
            # Col ranges from 0 to 9
            for col in range(COLS):
                if (row + col) % 2:
                    pygame.draw.rect(screen, DARK, (col * SQ_SIZE + PADDING, row * SQ_SIZE + PADDING, SQ_SIZE, SQ_SIZE))
                image = None
                match row, col:
                    case 1, 5:
                        image = pygame.image.load('images\specialCases\img_16.png')
                        image = pygame.transform.scale(image, (SQ_SIZE, SQ_SIZE))
                    case 2, 5:
                        image = pygame.image.load('images\specialCases\img_26.png')
                        image = pygame.transform.scale(image, (SQ_SIZE, SQ_SIZE))
                    case 2, 6:
                        image = pygame.image.load('images\specialCases\img_27.png')
                        image = pygame.transform.scale(image, (SQ_SIZE, SQ_SIZE))
                    case 2, 7:
                        image = pygame.image.load('images\specialCases\img_28.png')
                        image = pygame.transform.scale(image, (SQ_SIZE, SQ_SIZE))
                    case 2, 8:
                        image = pygame.image.load('images\specialCases\img_29.png')
                        image = pygame.transform.scale(image, (SQ_SIZE, SQ_SIZE))
                    case 2, 9:
                        image = pygame.image.load('images\specialCases\img_30.png')
                        image = pygame.transform.scale(image, (SQ_SIZE, SQ_SIZE))

                if image is not None:
                    image_rect = image.get_rect(topleft=(col * SQ_SIZE + PADDING, row * SQ_SIZE + PADDING))
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
        self.board[2].append(0)

    def get_piece(self, row, col):
        if row < ROWS and col < COLS:
            return self.board[row][col]

    def print_board(self, screen):
        screen.fill(BROWN)
        # pygame.draw.rect(screen, WHITE, pygame.Rect(PADDING-10, PADDING-10, SQ_SIZE * COLS + 20, SQ_SIZE * ROWS + 20), 10)
        pygame.draw.rect(screen, LIGHT, pygame.Rect(PADDING, PADDING, SQ_SIZE * COLS, SQ_SIZE * ROWS))

        self.draw_squares(screen)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(screen)

        for i in range(5 - self.black_left):
            pygame.draw.circle(screen, BLACK, (WIDTH - PADDING - i * SQ_SIZE, HEIGHT * 0.58), SQ_SIZE / 3)

        for i in range(5 - self.white_left):
            pygame.draw.circle(screen, WHITE, (PADDING + i * SQ_SIZE, HEIGHT * 0.58), SQ_SIZE / 3)

    def calc_valid_moves(self, houses, color):
        self.valid_moves = {}

        for row in range(ROWS):
            for col in range(COLS):
                piece = self.get_piece(row, col)
                if piece:
                    house_sum = col + houses
                    house_sub = col - houses

                    piece_1 = 0
                    piece_2 = 0
                    if row % 2 == 0:
                        if col + 1 <= 9:
                            piece_1 = self.get_piece(row, col+1)
                        elif col + 1 >= 10:
                            piece_1 = self.get_piece(row + 1, 9)
                    elif row == 1:
                        if col - 1 >= 0:
                            piece_1 = self.get_piece(row, col-1)
                        elif col - 1 < 0:
                            piece_1 = self.get_piece(row + 1, col+1)

                    if row % 2 == 0:
                        if col + 2 <= 9:
                            piece_2 = self.get_piece(row, col + 2)
                        elif col + 2 >= 10:
                            piece_2 = self.get_piece(row + 1, 8)
                    elif row == 1:
                        if col - 2 >= 0:
                            piece_2 = self.get_piece(row, col-2)
                        elif col - 2 < 0:
                            piece_2 = self.get_piece(row + 1, abs(col-2))

                    if piece_1 and piece_2:
                        if piece_1.color != piece.color and piece_2.color != piece.color and houses > 2:
                            continue

                    if piece.color == color:
                        move = None
                        if row == 0 and house_sum < 10:
                            move = {(row, col): (row, house_sum)}
                        elif row == 0 and house_sum >= 10:
                            move = {(row, col): (row + 1, 9 - (house_sum - 10))}
                            # self.valid_moves.append((piece.row + 1, 9 - (house_sum - 10)))
                        elif row == 1 and house_sub >= 0:
                            move = {(row, col): (row, house_sub)}
                            # self.valid_moves.append((piece.row, house_sub))
                        elif row == 1 and house_sub < 0:
                            move = {(row, col): (row + 1, abs(house_sub) - 1)}
                            # self.valid_moves.append((piece.row + 1, abs(house_sub) - 1))
                        elif row == 2 and house_sum < 6:
                            if house_sum == 5 and self.get_piece(2, 5) == 0:
                                move = {(row, col): (row, house_sum)}
                            elif house_sum != 5:
                                move = {(row, col): (row, house_sum)}

                        if row == 2 and col == 5:
                            if houses == 1:
                                move = {(row, col): house_humiliation}
                            elif houses == 2:
                                move = {(row, col): house_three_judges}
                            elif houses == 3:
                                move = {(row, col): house_two_judges}
                            elif houses == 4:
                                move = {(row, col): house_heru}
                            elif houses == 5:
                                move = {(row, col): (2, 10)}

                        elif (row, col) == house_three_judges and houses == 3:
                            move = {(row, col): (2, 10)}
                        elif (row, col) == house_two_judges and houses == 2:
                            move = {(row, col): (2, 10)}
                        elif (row, col) == house_heru and houses == 1:
                            move = {(row, col): (2, 10)}

                        if move is not None:
                            self.valid_moves.update(move)

        return self.valid_moves

    def special_houses(self, row, col):
        piece = self.get_piece(row, col)
        if (row, col) == house_humiliation:
            self.move(piece, house_second_life[0], house_second_life[1])  # Move to house of beauty

    def remove_piece(self, row, col, color):
        if color == BLACK:
            self.black_left -= 1
        else:
            self.white_left -= 1
        self.board[row][col] = 0

    def return_board(self):
        clean_board = []

        for row in range(ROWS):
            clean_board.append([])
            for col in range(COLS):
                clean_board[row].append([])
                piece = self.get_piece(row,col)
                if piece:
                    clean_board[row][col] = [piece.row, piece.col, piece.color]
                else:
                    clean_board[row][col] = 0

        clean_board[2].append(0)
        return clean_board
