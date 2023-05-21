import pygame
from random import randint
from .constants import WHITE, BLACK, SQ_SIZE, HEIGHT, PADDING


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

            rect_x = i * SQ_SIZE//1.5 + PADDING * 1.5
            rect_y = HEIGHT // 1.5

            pygame.draw.rect(screen, rect_color, (rect_x, rect_y, 20, 80))

    def calc_mov(self):
        white = 0
        moves = 0
        for i in self.sticks:
            if i == 0:
                white += 1
        if white == 0:
            moves = 5
        elif white == 2 or white == 3:
            moves = white
        else:
            moves = white
        return moves
    
    def play_again(self):
        moves = self.calc_mov()
        if moves != 2 and moves != 3:
            return True
        return True




            
            
            
            
            
        
                
