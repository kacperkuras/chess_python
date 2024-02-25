import sys
from Game import Game
import pygame

game = Game()

pygame.init()
screen = pygame.display.set_mode((game.BOARD_WIDTH, game.BOARD_HEIGHT))
pygame.display.set_caption('Chess')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("red")
    pygame.display.flip()
