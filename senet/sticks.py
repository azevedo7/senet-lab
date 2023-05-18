import pygame
from random import randint
from .constants import WHITE, BLACK


class Stick:
    def __init__(self):
        self.sticks = []

    def throw(self):
        self.sticks = []
        for i in range(4):
            self.sticks.append(randint(0, 1))

    # Function to draw the sticks
    def draw_sticks(self, screen):
        for i, value in enumerate(self.sticks):
            if value == 0:
                rect_color = WHITE
            else:
                rect_color = BLACK

            rect_x = i * 40 + 30
            rect_y = 250

            pygame.draw.rect(screen, rect_color, (rect_x, rect_y, 20, 80))

    def calc_mov(self):
        # TODO: Calculate number of houses to walk
        white = 0
        moves = 0
        for i in self.sticks:
            if i == 0:
                white += 1
        if white == 0:
            moves = 5
        elif white == 2 or white == 3:
            moves = white
            #play other
        else:
            moves = white
            #play again
        return moves
    
    def play_again(self):
        moves = self.calc_mov()
        if moves != 2 and moves != 3:
            return True
        return False




            
            
            
            
            
        
                
