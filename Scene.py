import pygame
from Button import Button

class Scene:
    TEXT_COLOR = 'black'
    def __init__(self, text, size, buttons=None, pos=None):
        self.font = pygame.font.Font('font/SigmarOne-Regular.ttf', size)
        self.text = text
        self.text_surf = self.font.render(self.text, True, Scene.TEXT_COLOR)
        self.surf = pygame.image.load('img/scenes/scene.png').convert()

        if not pos is None:
            text_x = (384 - self.text_surf.get_width()) // 2
            text_y = (768 - self.text_surf.get_height()) // 2
        else:
            text_x = pos[0]
            text_y = pos[1]

        self.rect = self.surf.get_rect(topleft=(0, 0))
        if not buttons is None:
            self.buttons = []
            for button  in buttons:
                self.buttons.append(Button(button[0], button[1]))
