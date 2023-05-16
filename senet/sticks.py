import pygame
from random import randint
from .constants import WHITE, BLACK


class Stick:
    def __init__(self):
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
        pass # TODO: Calculate number of houses to walk
        for i in self.sticks:
            if i == 1:
                black += 1
            
            
        
                
