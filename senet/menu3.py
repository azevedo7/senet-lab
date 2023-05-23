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

        image_back = pygame.image.load('images\img_back.png')
        image_back = pygame.transform.scale(image_back, (WIDTH, HEIGHT))
        screen.blit(image_back, (0,0))        
        #TEXT
        texto = font.render(f'MENU', True, BLACK)
        textRect = texto.get_rect(center = (WIDTH/2, HEIGHT*0.1))
        screen.blit(texto,(textRect))
        #BUTTONS
        button_1 = pygame.image.load('images\menu\play.png')
        button_1 = pygame.transform.scale(button_1, (200, 50))
        button_1_rect = button_1.get_rect(center=(WIDTH/2,HEIGHT*0.27))
        screen.blit(button_1, button_1_rect)

        button_2 = pygame.image.load('images\menu\load.png')
        button_2 = pygame.transform.scale(button_2, (200, 50))
        button_2_rect = button_2.get_rect(center=(WIDTH/2,HEIGHT*0.42))
        screen.blit(button_2, button_2_rect)

        button_3 = pygame.image.load('images\menu\_rules.png')
        button_3 = pygame.transform.scale(button_3, (200, 50))
        button_3_rect = button_3.get_rect(center=(WIDTH/2,HEIGHT*0.57))
        screen.blit(button_3, button_3_rect)

        button_4 = pygame.image.load('images\menu\exit.png')
        button_4 = pygame.transform.scale(button_4, (200, 50))
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
                  game_rules()
        if button_4_rect.collidepoint((pos)):
             if click:
                  pygame.quit()
                  exit()
        
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

            
        pygame.display.update()

            
def game_rules(screen):
    title=pygame.font.Font(None, 50)
    text=pygame.font.Font (None, 42)
    
    title_r = title.render("GAME RULES/COMPONENTS", True, (0,0,0))
    rule_1 = text.render ("The board consists of 3 rows and 10 columns that make a total of 30 squares", True, (0,0,0))
    rule_2 = text.render ("Each player has five pieces (brown or white) to play", True, (0,0,0))
    rule_3 = text.render ("There are 6 houses that have specific characteristics (16, 26,27,28,29,30)", True, (0,0,0))
    rule_4 = text.render ("The pieces have to be alternated, i.e. one white followed by one black.", True, (0,0,0))
    rule_5 = text.render ("The pieces must be moved in a line, the first line from left to right, the second from right to left, and the third again from left to right. In the third row, when it reaches the end, we remove the piece from the board.", True, (0,0,0))
    rule_6 = text.render ("A group of three or better dancers blocks the passage of opposing pieces", True, (0,0,0))
    rule_7 = text.render ("When a piece is forced to move backward, it may not attack an opposing piece.", True, (0,0,0))
    rule_8 = text.render ("The House of Second Life is considered a safe house (that is, a piece on that House may not be attacked", True, (0,0,0))
    rule_9 = text.render ("The House of Second Life is considered a safe house and grants the player an extra turn.", True, (0,0,0))
    rule_10 = text.render ("The House of Beauty grants the player an extra turn.", True, (0,0,0))
    rule_11 = text.render ("While a piece is on the House of Humiliation, no other piece is allowed to enter it.", True, (0,0,0))
    rule_12 = text.render ("A piece that falls on the House of Humiliation is sent back to the very first (farthest) house.", True, (0,0,0))
    rule_13 = text.render ("A piece that falls on the House of Humiliation is removed from the game and must be re-entered at the very first (farthest) house.", True, (0,0,0))
    rule_14 = text.render ("Pieces on the last three Houses are allowed to move forward in addition to bearing off.", True, (0,0,0))
    rule_15 = text.render ("The last three Houses and the House of Beauty are considered safe houses.", True, (0,0,0))
    rule_16 = text.render ("If a throw allows the player to bear a piece off, he must do so.", True, (0,0,0))
    rule_17 = text.render ("A player may bear off his pieces only once they are all on the last row of the board.", True, (0,0,0))
    
    screen.fill((255, 255, 255))
    screen.blit(title_r, (100, 90)) 
    screen.blit(rule_1, (100, 150))
    screen.blit(rule_2, (100, 180))
    screen.blit(rule_3, (100, 210))
    screen.blit(rule_4, (100, 240))
    screen.blit(rule_5, (100, 270))
    screen.blit(rule_6, (100, 300))
    screen.blit(rule_7, (100, 330))
    screen.blit(rule_8, (100, 360))
    screen.blit(rule_9, (100, 390))
    screen.blit(rule_10, (100, 420))
    screen.blit(rule_11, (100, 450))
    screen.blit(rule_12, (100, 480))
    screen.blit(rule_13, (100, 510))
    screen.blit(rule_14, (100, 540))
    screen.blit(rule_15, (100, 570))
    screen.blit(rule_16, (100, 600))
    screen.blit(rule_17, (100, 630))
    
    pygame.display.update()




