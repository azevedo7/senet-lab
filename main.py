import pygame
from senet.constants import WIDTH, HEIGHT, DARK, LIGHT, SQ_SIZE, WHITE, PADDING
from senet.menu import menu
from senet.start import start

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Senet')

def main():
    start(screen)
    pygame.mixer.music.set_volume(0.35)

    while True:
        menu(screen)


main()
