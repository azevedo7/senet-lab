import pygame

pygame.init()

def background(screen):

    background = pygame.image.load('"C:\Users\Jorge Costa\Desktop\imagem.png"')

    # Loop principal
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Desenhe a imagem de fundo na tela
        screen.blit(background, (0, 0))

        # Atualize a tela
        pygame.display.flip()

    pygame.quit()