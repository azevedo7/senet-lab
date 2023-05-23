import pygame
import random as rd
from senet.constants import BLACK, LIGHT

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