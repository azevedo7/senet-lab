import pygame
import sys
from senet.constants import LIGHT, WHITE, BLACK, WIDTH, HEIGHT

pygame.init()

pygame.display.set_caption("Menu")
font = font = pygame.font.Font("Newathenaunicode-EP3l.ttf", 20)


# Loop principal
def menu(screen):
    while True:
        screen.fill(LIGHT)
        texto = font.render(f'MENU', True, BLACK)
        textRect = texto.get_rect(center = (WIDTH/2, HEIGHT*0.1))
        screen.blit(texto,(textRect))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            
        pygame.display.update()

            




