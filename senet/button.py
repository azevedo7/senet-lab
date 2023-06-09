import pygame
from .constants import WIDTH, HEIGHT


class Button:
    def __init__(self, image, pos, text_input, font, base_color, hovering_color, y):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos + y))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

    def changeImage(self, image):
        self.image = image

class ButtonOnly:
    def __init__(self, image, pos):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            return True
        return False
    
    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)

def soundButton(screen):
    if pygame.mixer.music.get_volume() < 0.1:
        sound_image = pygame.transform.rotozoom(pygame.image.load('images/menu/sound_off.png'), 0, 0.15)
    else:
        sound_image = pygame.transform.rotozoom(pygame.image.load('images/menu/sound_on.png'), 0, 0.15)
    sound_button = ButtonOnly(sound_image, (50, 50))
    sound_button.update(screen)
    return sound_button


            
def exit_game():
    button_font = pygame.font.Font("Senet_font-Regular.ttf", 34)
    button_image = pygame.transform.rotozoom(pygame.image.load('images\menu\img_none.png'), 0, 0.3)
    exit_button = Button(button_image, pos=(WIDTH / 2, HEIGHT * 0.90), text_input='BACK',
                         font=button_font, base_color="black", hovering_color="white", y=-7)
    return exit_button