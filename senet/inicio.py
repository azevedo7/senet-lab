import pygame
from menu import menu
pygame.init

def inicio(screen):
  pygame.image.load("Meu projeto(1).png")
  # Defina a fonte do texto
  base_font = pygame.font.Font(None, 32)
   menu = [{"text": "NEXT STEP", "pos": (WIDTH // 2, HEIGHT // 2 - 75)}
           {"text": "Worked done by: César Faria, Diana Costa, João Azevedo", "pos": (WIDTH // 2, HEIGHT // 2 - 75)}]
  
  while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if a menu item was clicked
                for item in menu:
                    if item["rect"].collidepoint(event.pos):
                        if item["text"] == "next":
                          menu()
                          return True
                            