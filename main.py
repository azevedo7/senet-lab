import pygame
from senet.constants import WIDTH, HEIGHT, DARK, LIGHT, SQ_SIZE, WHITE, PADDING
from senet.board import Board
from senet.sticks import Stick
from senet.menu3 import menu
from senet.game import Game
from senet.start import start
from senet.rules import game_rules
from sys import exit

FPS = 30
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Senet')


#   -Piece movement
# TODO:
#       Move animation
#       End game condition
#            -Check if every piece of one color is gone

def select_piece(pos):
    mouse_x, mouse_y = pygame.mouse.get_pos()

    row = (mouse_y - PADDING) // SQ_SIZE
    col = (mouse_x - PADDING) // SQ_SIZE

    return row, col


def main():
    clock = pygame.time.Clock()
    game = Game(screen)

    run = start(screen)
    # run = menu(screen)

    while run:
        round_over = False
        game.sticks.throw()
        selected = 0
        while not round_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = select_piece(pos)
                    game.select(row, col)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game.selected = None

            game.update()
            game.sticks.draw_sticks(screen)

            pygame.display.update()

            clock.tick(FPS)

    pygame.quit()


main()
