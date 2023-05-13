import pygame
from random import randint

class Stick:
    def __init__(self):
        self.sticks = []
        for i in range(4):
            self.sticks.append(randint(0, 1))

    # Function to draw the sticks
    def draw_sticks(self):
        pass