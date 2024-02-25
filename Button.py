import pygame.font


class Button:
    BUTTON_WIDTH = 250
    BUTTON_HEIGHT = 80
    TEXT_COLOR = 'white'

    def __init__(self, text, pos):
        self.font = pygame.font.Font('font/SigmarOne-Regular.ttf', 35)
        button_image = pygame.image.load('img/button/button.png').convert_alpha()
        self.text = text
        self.text_surf = self.font.render(self.text, True, Button.TEXT_COLOR)
        text_x = (Button.BUTTON_WIDTH - self.text_surf.get_width()) // 2
        text_y = (Button.BUTTON_HEIGHT - self.text_surf.get_height()) // 2

        self.surf = button_image
        self.surf.blit(self.text_surf, (text_x, text_y))
        self.rect = self.surf.get_rect(topleft=(pos[0], pos[1]))


