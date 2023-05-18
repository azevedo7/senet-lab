import pygame
from senet.constants import WIDTH, HEIGHT, DARK, LIGHT, SQ_SIZE
from senet.board import Board
from senet.sticks import Stick
from senet.menu import menu
from senet.launch import back

FPS = 30
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Senet')

#   -Piece movement
# TODO:
#       Check if movement is valid
#       Show valid movements
#       Selection animation

def select_piece(pos):
    mouse_x, mouse_y = pygame.mouse.get_pos()

    row = mouse_y // SQ_SIZE
    col = mouse_x // SQ_SIZE
    return row, col

def main():
    clock = pygame.time.Clock()
    board = Board()
    board.create_board()

    run = back(screen)


    while run:
        round_over = False
        sticks = Stick()
        sticks.play_again()
        selected = 0
        while not round_over:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    round_over = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if selected == 0:
                        row, col = select_piece(pos)
                        piece = board.get_piece(row, col)
                        selected = 1
                    elif selected == 1:
                        row, col = select_piece(pos)
                        if piece:
                            board.move(piece, row, col)
                        selected = 0


            board.draw_squares(screen)
            board.print_board(screen)
            sticks.draw_sticks(screen)



            pygame.display.update()

    pygame.quit()


main()
