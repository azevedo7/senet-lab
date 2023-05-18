import pygame
from .constants import WIDTH, HEIGHT, LIGHT
from senet.launch import back

pygame.init()


def menu(screen):
    # Set up the window
    # Set up the fonts
    font = pygame.font.Font(None, 36)

    # Set up the menu items
    menu = [{"text": "Start Game", "pos": (WIDTH // 2, HEIGHT // 2 - 75)},
            {"text": "Load Game from a file ", "pos": (WIDTH // 2, HEIGHT // 2 - 25)},
            {"text": "Display a Game Description", "pos": (WIDTH // 2, HEIGHT // 2 + 25)},
            {"text": "Exit", "pos": (WIDTH // 2, HEIGHT // 2 + 75)}]

    # Game loop

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if a menu item was clicked
                for item in menu:
                    if item["rect"].collidepoint(event.pos):
                        if item["text"] == "Start Game":
                            return True
                            ##################################

                        elif item["text"] == "Load Game from a file":
                            print("Openning options...")
                            return False

                        elif item["text"] == "Rules Game":
                            print("Openning rules...")
                            ##################################
                            return False

                        elif item["text"] == "Exit":
                            pygame.quit()
                            exit()

                # Draw the menu items
        screen.fill(LIGHT)
        for item in menu:
            text = font.render(item["text"], False, (0, 0, 0))
            item["rect"] = text.get_rect(center=item["pos"])
            screen.blit(text, item["rect"])

        # Update the display
        pygame.display.update()
