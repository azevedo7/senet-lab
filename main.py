import pygame
from senet.constants import WIDTH, HEIGHT, DARK, LIGHT, SQ_SIZE
from senet.board import Board
from senet.sticks import Stick
from senet.menu import menu
from senet.game import Game
from senet.launch import back

FPS = 30
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Senet')


#   -Piece movement
# TODO:
#       Show valid movements
#       Selection animation

def select_piece(pos):
    mouse_x, mouse_y = pygame.mouse.get_pos()

    row = mouse_y // SQ_SIZE
    col = mouse_x // SQ_SIZE
    return row, col


def main():
    clock = pygame.time.Clock()
    game = Game(screen)

    run = back(screen)
    run = menu(screen)

    while run:
        round_over = False
        game.sticks.throw()
        selected = 0
        while not round_over:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    round_over = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = select_piece(pos)
                    game.select(row, col)
                if event.type == pygame.K_ESCAPE:
                    game.selected = None

            game.update()
            game.sticks.draw_sticks(screen)

            pygame.display.update()

    pygame.quit()


main()
