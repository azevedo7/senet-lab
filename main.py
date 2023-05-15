import pygame
from senet.constants import WIDTH, HEIGHT, DARK, LIGHT
from senet.board import Board
from senet.sticks import Stick
from senet.menu import menu

FPS = 30
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Senet')

# TODO:
#   -Piece movement
#       Check if movement is valid
#       Show valid movements
#       Selection animation
#   -Sticks calc_mov function
#   -Implement menu


def main():
    clock = pygame.time.Clock()
    board = Board()
    board.create_board()

    run = menu(screen)

    while run:
        round_over = False
        sticks = Stick()
        while not round_over:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    round_over = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    board.select_piece()
                    pass

            board.draw_squares(screen)
            board.print_board(screen)
            sticks.draw_sticks(screen)

            pygame.display.update()

    pygame.quit()


main()
