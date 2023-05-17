import pygame
import random


pygame.init()
def nome(screen):
    pygame.dispplay.set_caption("Player name:")
    
    def display_text(text, position):
        font=pygame.font.Font(None, 36)
        text_surface=font.render(text, True, (255,255,255))
        screen.blit(text_surface, position)
        
    user_name = ""
    first_player = ""
    while True: 
        screen.fill((0,0,0))
        display_text("Player name: " + user_name, (50,50))
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    if random.randint (0,1) == 1:
                        first_player = user_name
                    else:
                        first_player = "BOT"
                        
                    print("Player Name: ", user_name)
                    print("First Player: ", first_player)
                    pygame.quit()
                    exit()
                elif event.key==pygame.K_BACKSPACE:
                    user_name=user_name[:-1]
                else:
                    user_name+=event.unicode
        pygame.display.flip()