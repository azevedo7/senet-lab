import pygame
from .constants import WIDTH, HEIGHT, SQ_SIZE
pygame.init()

def back(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True

        
        image_back = pygame.image.load('images\img_back.png')
        image_back = pygame.transform.scale(image_back, (WIDTH, HEIGHT))
        screen.blit(image_back, (0,0))

        pygame.display.update()


def title(self):
    image_title = pygame.image.load('\images\img_senet.png')


def made_by(self):
    made = {"text": "Made by", "pos": (WIDTH // 2, HEIGHT // 2 - 75) }