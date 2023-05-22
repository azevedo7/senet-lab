import pygame
import sys
from senet.constants import LIGHT, WHITE, BLACK, WIDTH, HEIGHT
from senet.rules import game_rules

pygame.init()

pygame.display.set_caption("Menu")
font = font = pygame.font.Font("Newathenaunicode-EP3l.ttf", 20)
click = False

# Loop principal
def menu(screen):
    while True:
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                     click = True



        image_back = pygame.image.load('images\img_back.png')
        image_back = pygame.transform.scale(image_back, (WIDTH, HEIGHT))
        screen.blit(image_back, (0,0))        
        #TEXT
        texto = font.render(f'MENU', True, BLACK)
        textRect = texto.get_rect(center = (WIDTH/2, HEIGHT*0.1))
        screen.blit(texto,(textRect))
        #BUTTONS
        button_1 = pygame.image.load('images\menu\img_none.png')
        button_1 = pygame.transform.scale(button_1, (300, 100))
        button_1_rect = button_1.get_rect(center=(WIDTH/2,HEIGHT*0.27))
        screen.blit(button_1, button_1_rect)

        button_2 = pygame.image.load('images\menu\img_none.png')
        button_2 = pygame.transform.scale(button_2, (300, 100))
        button_2_rect = button_2.get_rect(center=(WIDTH/2,HEIGHT*0.42))
        screen.blit(button_2, button_2_rect)

        button_3 = pygame.image.load('images\menu\img_none.png')
        button_3 = pygame.transform.scale(button_3, (300, 100))
        button_3_rect = button_3.get_rect(center=(WIDTH/2,HEIGHT*0.57))
        screen.blit(button_3, button_3_rect)

        button_4 = pygame.image.load('images\menu\img_none.png')
        button_4 = pygame.transform.scale(button_4, (300, 100))
        button_4_rect = button_4.get_rect(center=(WIDTH/2,HEIGHT*0.72))
        screen.blit(button_4, button_4_rect)
        #CHOOSE
        pos = pygame.mouse.get_pos()
        
        if button_1_rect.collidepoint((pos)):
             if click:
                  return True
        if button_2_rect.collidepoint((pos)):
             if click:
                  pass
        if button_3_rect.collidepoint((pos)):
             if click:
                  game_rules(screen)
        if button_4_rect.collidepoint((pos)):
             if click:
                  pygame.quit()
                  exit()
        

        
            
        pygame.display.update()

            




