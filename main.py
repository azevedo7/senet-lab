import pygame
from senet.constants import WIDTH, HEIGHT, DARK, LIGHT, SQ_SIZE, WHITE, PADDING
from senet.menu import menu
from senet.start import start


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
    start(screen)

    while True:
        menu(screen)


main()
