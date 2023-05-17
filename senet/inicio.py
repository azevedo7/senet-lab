import pygame
pygame.init

def inicio(screen):

  # Defina a fonte do texto
    base_font = pygame.font.Font(None, 32)

    # Variável para armazenar o texto do usuário
    user_text = "SENET"

    # Loop principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

        # Limpe a tela
        screen.fill((255, 255, 255))

        # Renderize o texto e exiba-o na tela
        text_surface = base_font.render(user_text, True, (0, 0, 0))
        screen.blit(text_surface, (10, 10))

        # Atualize a tela
        pygame.display.update()