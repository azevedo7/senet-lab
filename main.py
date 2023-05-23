import pygame
from senet.constants import WIDTH, HEIGHT, DARK, LIGHT, SQ_SIZE, WHITE, PADDING
<<<<<<< HEAD
<<<<<<< HEAD
from senet.board import Board
from senet.sticks import Stick
from senet.menu3 import menu
from senet.game import Game
from senet.start import start
from senet.rules import game_rules
from sys import exit
=======
from senet.menu3 import menu
from senet.game import Game
>>>>>>> parent of 18345ff (Update)
=======
from senet.menu3 import menu
from senet.game import Game
>>>>>>> parent of 18345ff (Update)

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

<<<<<<< HEAD
    row = (mouse_y - PADDING) // SQ_SIZE
    col = (mouse_x - PADDING) // SQ_SIZE

    return row, col

def main():
<<<<<<< HEAD
    clock = pygame.time.Clock()
    game = Game(screen)

    run = start(screen)
    # run = menu(screen)
=======
=======
def main():
>>>>>>> parent of 18345ff (Update)
    game = Game(screen)

    while True:
        menu(screen, game)
<<<<<<< HEAD
>>>>>>> parent of 18345ff (Update)
=======
>>>>>>> parent of 18345ff (Update)

    while run:
        game.sticks.throw()
        while not game.over:
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
            clock.tick(FPS)
        game.over = start(screen)

main()
