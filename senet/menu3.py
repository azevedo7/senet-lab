import pygame
import sys
<<<<<<< HEAD
<<<<<<< HEAD
from senet.constants import LIGHT, WHITE, BLACK, WIDTH, HEIGHT
from senet.rules import game_rules
=======
from senet.constants import *
from senet.button import Button
>>>>>>> parent of 18345ff (Update)
=======
from senet.constants import *
from senet.button import Button
>>>>>>> parent of 18345ff (Update)

pygame.init()

pygame.display.set_caption("Menu")
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======
>>>>>>> parent of 18345ff (Update)
font = pygame.font.Font("Newathenaunicode-EP3l.ttf", 20)
button_font = pygame.font.Font("Senet_font-Regular.ttf", 34)


# Loop principal
def menu(screen, game):
    while True:
        pos = pygame.mouse.get_pos()

        image_back = pygame.image.load('images\img_back.png')
        image_back = pygame.transform.scale(image_back, (WIDTH, HEIGHT))
        screen.blit(image_back, (0, 0))
        # TEXT
        texto = font.render(f'MENU', True, BLACK)
        text_rect = texto.get_rect(center=(WIDTH / 2, HEIGHT * 0.1))
        screen.blit(texto, text_rect)

        # BUTTONS
        button_image = pygame.transform.rotozoom(pygame.image.load('images\menu\img_none.png'), 0, 0.3)

        distance = 0.17
        play_button = Button(button_image, pos=(WIDTH / 2, HEIGHT * 0.27), text_input='PLAY',
                             font=button_font, base_color="black", hovering_color="white")
        load_button = Button(button_image, pos=(WIDTH / 2, HEIGHT * (0.27 + distance * 1)), text_input='LOAD',
                             font=button_font, base_color="black", hovering_color="white")
        rules_button = Button(button_image, pos=(WIDTH / 2, HEIGHT * (0.27 + distance * 2)), text_input='RULES',
                              font=button_font, base_color="black", hovering_color="white")
        exit_button = Button(button_image, pos=(WIDTH / 2, HEIGHT * (0.27 + distance * 3)), text_input='EXIT',
                             font=button_font, base_color="black", hovering_color="white")

        for button in [play_button, load_button, rules_button, exit_button]:
            button.changeColor(pos)
            button.update(screen)
<<<<<<< HEAD
>>>>>>> parent of 18345ff (Update)
=======
>>>>>>> parent of 18345ff (Update)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
<<<<<<< HEAD
<<<<<<< HEAD
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




=======
=======
>>>>>>> parent of 18345ff (Update)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(pos):
                    play(game)
                if load_button.checkForInput(pos):
                    pass
                if rules_button.checkForInput(pos):
                    game_rules(screen)
                if exit_button.checkForInput(pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def play(game):
    clock = pygame.time.Clock()

    game.sticks.throw()
    while not game.over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = select_piece(pos)
                game.select(row, col)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game.selected = None

        game.update()
        clock.tick(FPS)

    return


def select_piece(pos):
    mouse_x, mouse_y = pygame.mouse.get_pos()

    row = (mouse_y - PADDING) // SQ_SIZE
    col = (mouse_x - PADDING) // SQ_SIZE

    return row, col


def game_rules(screen):
    font = pygame.font.Font(None, 26)
    margin = 26  # Vertical spacing between text lines
    y = 15  # Initial y-coordinate for the first line
    x = 15

    texts = [
        "GAME RULES/COMPONENTS",
        "",
        "The board consists of 3 rows and 10 columns that make a total of 30 squares",
        "Each player has five pieces (brown or white) to play",
        "There are 6 houses that have specific characteristics (16, 26, 27, 28, 29, 30)",
        "The pieces have to be alternated, i.e. one white followed by one black.",
        "The pieces must be moved in a line, the first line from left to right, the second from right to left, ",
        "and the third again from left to right. In the third row, when it reaches the end, we remove the piece from ",
        "   the board.",
        "A group of three or better dancers blocks the passage of opposing pieces",
        "When a piece is forced to move backward, it may not attack an opposing piece.",
        "The House of Second Life is considered a safe house (that is, a piece on that House may not be attacked",
        "The House of Second Life is considered a safe house and grants the player an extra turn.",
        "The House of Beauty grants the player an extra turn.",
        "While a piece is on the House of Humiliation, no other piece is allowed to enter it.",
        "A piece that falls on the House of Humiliation is sent back to the very first (farthest) house.",
        "A piece that falls on the House of Humiliation is removed from the game and must be re-entered at the very ",
        "   first (farthest) house.",
        "Pieces on the last three Houses are allowed to move forward in addition to bearing off.",
        "The last three Houses and the House of Beauty are considered safe houses.",
        "If a throw allows the player to bear a piece off, he must do so.",
        "A player may bear off his pieces only once they are all on the last row of the board."
    ]

    while True:
        screen.fill((255, 255, 255))
        y_pos = y

        for text in texts:
            rendered_text = font.render(text, True, (0, 0, 0))
            screen.blit(rendered_text, (x, y_pos))
            y_pos += margin

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return
<<<<<<< HEAD
>>>>>>> parent of 18345ff (Update)
=======
>>>>>>> parent of 18345ff (Update)
