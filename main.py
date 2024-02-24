import sys

import pygame

pygame.init()
screen = pygame.display.set_mode((768, 768))
pygame.display.set_caption('Chess')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("red")
    pygame.display.flip()
