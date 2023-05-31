import sys
from senet.constants import *
from senet.button import *
from senet.game import Game
import random as rd
from ast import literal_eval
from senet.pieces import Piece
from random import randint

font = None
button_font = None
button_image = None


def menu(screen):
    button_font = pygame.font.Font("Senet_font-Regular.ttf", 34)
    button_image = pygame.transform.rotozoom(pygame.image.load('images\menu\img_none.png'), 0, 0.3)

    pygame.init()
    pygame.display.set_caption("Menu")

    while True:
        pos = pygame.mouse.get_pos()
        image_back = pygame.image.load('images\img_back.png')
        image_back = pygame.transform.scale(image_back, (WIDTH, HEIGHT))
        screen.blit(image_back, (0, 0))

        # TEXT
        texto = button_font.render(f'MENU', True, BLACK)
        text_rect = texto.get_rect(center=(WIDTH / 2, HEIGHT * 0.1))
        screen.blit(texto, text_rect)

        # BUTTONS

        distance = 0.17
        play_button = Button(button_image, pos=(WIDTH / 2, HEIGHT * 0.27), text_input='PLAY',
                             font=button_font, base_color="black", hovering_color="white", y=-7)
        load_button = Button(button_image, pos=(WIDTH / 2, HEIGHT * (0.27 + distance * 1)), text_input='LOAD',
                             font=button_font, base_color="black", hovering_color="white", y=-7)
        rules_button = Button(button_image, pos=(WIDTH / 2, HEIGHT * (0.27 + distance * 2)), text_input='RULES',
                              font=button_font, base_color="black", hovering_color="white", y=-7)
        exit_button = Button(button_image, pos=(WIDTH / 2, HEIGHT * (0.27 + distance * 3)), text_input='EXIT',
                             font=button_font, base_color="black", hovering_color="white", y=-7)

        for button in [play_button, load_button, rules_button, exit_button]:
            button.changeColor(pos)
            button.update(screen)
        sound_button = soundButton(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(pos):
                    # play(game, screen)
                    init_game(screen)
                if load_button.checkForInput(pos):
                    loadGame(screen)
                if rules_button.checkForInput(pos):
                    game_rules(screen)
                if exit_button.checkForInput(pos):
                    pygame.quit()
                    sys.exit()
                if sound_button.checkForInput(pos):
                    if pygame.mixer.music.get_volume() <= 0.1:
                        pygame.mixer.music.set_volume(0.35)
                    else:
                        pygame.mixer.music.set_volume(0)

        pygame.display.update()


def play(game, screen):
    clock = pygame.time.Clock()
    EXIT_BUTTON = exit_game()
    if not game.game_is_loaded:
        game.sticks.throw()
    game.game_is_loaded = 0

    turns = [BLACK, WHITE]
    game.turn = turns[randint(0, 1)]

    bot_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(bot_timer, 900)
    while not game.over:
        pos = pygame.mouse.get_pos()

        game.update()
        EXIT_BUTTON.changeColor(pos)
        EXIT_BUTTON.update(screen)
        pygame.display.update()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                saveGame(screen, game)
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EXIT_BUTTON.checkForInput(pos):
                    saveGame(screen, game)
                    return
                row, col = select_piece()
                if not (game.bot and game.turn == BLACK):
                    game.select(row, col)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game.selected = None
            if event.type == bot_timer:
                game.bot_play()
        game.update()
    win_screen(screen, game)
    return


def select_piece():
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
    button_font = pygame.font.Font("Senet_font-Regular.ttf", 24)
    button_image = pygame.transform.rotozoom(pygame.image.load('images\menu\img_none.png'), 0, 0.2)

    return_button = Button(button_image, pos=(WIDTH * 0.90, HEIGHT * 0.90), text_input='BACK',
                           font=button_font, base_color="black", hovering_color="white", y=-7)

    while True:
        screen.fill((255, 255, 255))
        y_pos = y
        pos = pygame.mouse.get_pos()
        return_button.changeColor(pos)

        for text in texts:
            rendered_text = font.render(text, True, (0, 0, 0))
            screen.blit(rendered_text, (x, y_pos))
            y_pos += margin
        return_button.update(screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_button.checkForInput(pos):
                    menu(screen)


def init_game(screen):
    button_font = pygame.font.Font("Senet_font-Regular.ttf", 34)
    button_image = pygame.transform.rotozoom(pygame.image.load('images/menu/stone_button.png'), 0, 0.15)
    player_name_image = pygame.transform.rotozoom(pygame.image.load('images/menu/stone_button2.png'), 0, 0.3)
    continue_image = pygame.transform.rotozoom(pygame.image.load('images/menu/metal_button.png'), 0, 0.20)

    board_image = pygame.transform.rotozoom(pygame.image.load('images/menu/board.png'), 0, 0.4)
    board_rect = board_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    bullet_on = pygame.transform.rotozoom(pygame.image.load('images/menu/bullet_point_on.png'), 0, 0.25)
    bullet_off = pygame.transform.rotozoom(pygame.image.load('images/menu/bullet_point_off.png'), 0, 0.25)
    bot = 0

    player_bullet = Button(bullet_on, pos=(WIDTH * 0.3, HEIGHT * 0.45), text_input='',
                           font=button_font, base_color="black", hovering_color="black", y=0)
    bot_bullet = Button(bullet_off, pos=(WIDTH * 0.7, HEIGHT * 0.45), text_input='',
                        font=button_font, base_color="black", hovering_color="black", y=0)

    # Images and Buttons
    player_button = Button(button_image, pos=(WIDTH * 0.3, HEIGHT * 0.3), text_input='PLAYER',
                           font=button_font, base_color="black", hovering_color="black", y=0)
    bot_button = Button(button_image, pos=(WIDTH * 0.7, HEIGHT * 0.3), text_input='BOT',
                        font=button_font, base_color="black", hovering_color="black", y=0)

    continue_button = Button(continue_image, pos=(WIDTH // 2, HEIGHT * 0.80), text_input='CONTINUE',
                             font=button_font, base_color="black", hovering_color="white", y=-2)

    player_name = "Click to type"
    name_color = BLACK
    write_name = 0
    text = pygame.font.Font(None, 27)
    activation = True
    option_players = ["Player", "BOT"]
    random_player = rd.choice(option_players)
    write_text = text.render("The first player is:" + random_player, True, BLACK)

    while activation:
        pos = pygame.mouse.get_pos()
        player_name_button = Button(player_name_image, pos=(WIDTH // 2, HEIGHT * 0.6), text_input=f"{player_name}"
                                    , font=button_font, base_color=name_color, hovering_color='black', y=0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN and write_name:
                if event.key == pygame.K_RETURN:
                    activation = False
                    player_name = "Anonymous Player" if (not player_name or player_name == "Click here to type")\
                        else player_name
                    game = Game(screen, bot)
                    game.player_name = player_name
                    play(game, screen)
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[: -1]
                else:
                    player_name += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bot_bullet.checkForInput(pos):
                    player_bullet.changeImage(bullet_off)
                    bot_bullet.changeImage(bullet_on)
                    bot = 1
                if player_bullet.checkForInput(pos):
                    player_bullet.changeImage(bullet_on)
                    bot_bullet.changeImage(bullet_off)
                    bot = 0
                if player_name_button.checkForInput(pos):
                    if player_name == "Click to type":
                        player_name = ''
                    write_name = 1
                    name_color = WHITE
                if not player_name_button.checkForInput(pos):
                    write_name = 0
                    name_color = BLACK
                if continue_button.checkForInput(pos):
                    play(Game(screen, bot), screen)
                    return


        screen.fill((255, 255, 255))
        screen.blit(board_image, board_rect)

        for button in [player_button, bot_button, player_bullet, bot_bullet, continue_button, player_name_button]:
            button.update(screen)
            button.changeColor(pos)

        # write_name = text.render("Enter your name: " + player_name, True, BLACK)
        # screen.blit(write_text, (40, 40))
        # screen.blit(write_name, (40, 80))
        pygame.display.update()

    return player_name

def win_screen(screen, game):
    clock = pygame.time.Clock()
    font = pygame.font.Font("Senet_font-Regular.ttf", 60)
    exit_button = exit_game()

    # Render the text
    if game.winner == BLACK:
        text = font.render("Black Wins", True, (255, 255, 255))  # White color
    else:
        text = font.render("White Wins", True, (255, 255, 255))  # White color

    # Center the text on the screen
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # Draw a translucent rectangle behind the text
    rect_width, rect_height = text_rect.width + 40, text_rect.height + 40
    rect = pygame.Rect((WIDTH - rect_width) // 2, (HEIGHT - rect_height) // 2, rect_width, rect_height)
    pygame.draw.rect(screen, (0, 0, 0, 128), rect)

    # Draw the text on the screen
    screen.blit(text, text_rect)

    # Wait for the user to close the window
    while True:
        pos = pygame.mouse.get_pos()
        exit_button.update(screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.checkForInput(pos):
                    return
        clock.tick(FPS)


def saveGame(screen, game):
    SAVE_GAME = input("introduza o nome do ficheiro em que pretenda guardar o jogo")

    try:
        with open('docs/readme.txt', 'x+') as f:
            file = open("%s.py" % SAVE_GAME, 'w')
    except FileNotFoundError:
        file = open("%s.txt" % SAVE_GAME, 'w')
    save_list = []

    save_list.append(game.player_name)
    save_list.append(game.bot)
    save_list.append(game.sticks.calc_mov())
    save_list.append(game.board.return_board())
    save_list.append(game.turn)

    file.write(str(save_list))
    # file.write("Player =" + str(game.player_name))
    # file.write("Sticks =" + str(game.sticks))
    # file.write("Pieces position=" + str(game.player_name))
    # file.write(" =" + str(game.board))


def loadGame(screen):
    file_name = input("Indique o nome do ficheiro que pretende ler:") + ".txt"

    with open(file_name, 'r') as file:
        content = file.read()

    converted_list = literal_eval(content)
    game = Game(screen, converted_list[1])

    game_board = []
    save_board = converted_list[3]
    game.board.board = []


    for row in range(ROWS):
        game_board.append([])
        game.board.board.append([])
        for col in range(COLS):

            piece_details = save_board[row][col]
            if piece_details != 0:
                game.board.board[row].append(Piece(piece_details[0], piece_details[1], piece_details[2]))
                pass
            else:
                game.board.board[row].append(0)

    while True:
        game.sticks.throw()
        if game.sticks.calc_mov() == converted_list[2]:
            break

    game.turn = converted_list[4]
    game.game_is_loaded = 1
    play(game, screen)