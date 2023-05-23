import pygame
import sys
from senet.constants import *
from senet.button import Button
from senet.game import Game
import random as rd

# Loop principal
def menu(screen):
    game = Game(screen)

    pygame.init()

    pygame.display.set_caption("Menu")
    font = pygame.font.Font("Newathenaunicode-EP3l.ttf", 20)
    button_font = pygame.font.Font("Senet_font-Regular.ttf", 34)

    pygame.mixer.music.set_volume(0.35)

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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(pos):
                    play(game, screen)
                if load_button.checkForInput(pos):
                    pass
                if rules_button.checkForInput(pos):
                    game_rules(screen)
                if exit_button.checkForInput(pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def play(game, screen):
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
    game = Game(screen)
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


def player_name (screen):
    jogador = ""
    text= pygame.font.Font (None, 27)
    activation = True
    option_players=["Player","BOT"]
    random_player = rd.choice(option_players)
    write_text= text.render("The first player is:" + random_player, True, BLACK)
    
    while activation:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    activation=False
                    player = "Anonymous Player" if not player else player
                elif event.key == pygame.K_BACKSPACE:
                    player = player [: -1]
                else:
                    player += event.unicode
                    
    screen.fill(LIGHT)
    write_name= text.rendes("Enter your name: " + player, True, BLACK)
    screen.blit (write_text, (40,40))
    screen.blit (write_name, (40,80))
    pygame.display.update()
    
    return  player_name
