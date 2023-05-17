import pygame

pygame.init()

def menu2(screen): 
    import pygame

    pygame.init()

    # Definição das opções do menu
    menu_options = ['Start Game', 'Load Game', 'Rules Game', 'Exit']

    # Definição das cores utilizadas no menu
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (128, 128, 128)
    PURPLE= (255, 0, 255)

    # Definição das dimensões da janela do jogo
    WINDOW_WIDTH = 900
    WINDOW_HEIGHT = 500
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # Definição da fonte utilizada no menu
    font = pygame.font.SysFont('Comic Sans MS', 18)

    # Definição dos botões
    buttons = []
    for i in range(len(menu_options)):
        button = pygame.Rect(WINDOW_WIDTH/2 - 100, (i+1)*100 - 40, 200, 80)
        buttons.append(button)

    # Loop principal do jogo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(buttons)):
                    if buttons[i].collidepoint(pygame.mouse.get_pos()):
                        if i == 0:
                            print('Option A selected')
                    elif i == 1:
                            print('Option B selected')
                    elif i == 2:
                            print('Option C selected')
                    elif i == 3:
                            pygame.quit()
                            quit()

        window.fill(WHITE)
        for i in range(len(menu_options)):
            if buttons[i].collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(window, PURPLE, buttons[i])
            else:
                pygame.draw.rect(window, GRAY, buttons[i])
            text = font.render(menu_options[i], True, WHITE)
            text_rect = text.get_rect(center=buttons[i].center)
            window.blit(text, text_rect)
            
        pygame.display.update()