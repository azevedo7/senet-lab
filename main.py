import pygame
from sys import exit
from senet.constants import WIDTH, HEIGHT, DARK, LIGHT
from senet.board import Board
from senet.pieces import Piece
from senet.sticks import Stick

FPS = 30
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Senet')

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    board.create_board()
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.draw_squares(screen)
        board.print_board(screen)

        pygame.display.update()


    pygame.quit()

main()