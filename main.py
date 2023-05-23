import pygame
from senet.constants import WIDTH, HEIGHT, DARK, LIGHT, SQ_SIZE, WHITE, PADDING
from senet.menu3 import menu
from senet.game import Game


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Senet')


#   -Piece movement
# TODO:
#       Move animation
#       End game condition
#            -Check if every piece of one color is gone
#       Restart game when a game ends


def main():
    game = Game(screen)

    while True:
        menu(screen, game)


main()
