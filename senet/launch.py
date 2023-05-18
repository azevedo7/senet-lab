import pygame
from .constants import WIDTH, HEIGHT, SQ_SIZE, BLACK, WHITE
from senet.menu import menu
pygame.init()

def back(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True

        font = pygame.font.Font("Newathenaunicode-EP3l.ttf", 20)

        image_back = pygame.image.load('images\img_back.png')
        image_back = pygame.transform.scale(image_back, (WIDTH, HEIGHT))
        screen.blit(image_back, (0,0))

        image_title = pygame.image.load('images\img_senet.png')
        image_title = pygame.transform.scale(image_title, (211, 45))
        image_title_rect = image_title.get_rect(center=(WIDTH/2,HEIGHT*0.17))
        screen.blit(image_title, image_title_rect)

        
        texto = font.render(f'Press any key to continue!', True, BLACK)
        textRect = texto.get_rect(center = (WIDTH/2, HEIGHT*0.6))
        screen.blit(texto,(textRect))


        texto = font.render(f'Made by César Faria, Diana Costa, João Azevedo', True, WHITE)
        textRect1 = texto.get_rect(center = (WIDTH/2, HEIGHT*0.95))
        screen.blit(texto,(textRect1))

    

        pygame.display.update()