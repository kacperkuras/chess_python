import pygame


class BoardSquare:
    white_square = pygame.image.load('img/board/white.png').convert()
    black_square = pygame.image.load('img/board/black.png').convert()
    attack_square = pygame.image.load('img/board/attack.png').convert()
    move_square = pygame.image.load('img/board/move.png').convert()
    test_square = pygame.image.load('img/board/test.png').convert()

    board_squares = []
    board_squares_pos = []

    def __init__(self, image, color, x, y):
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.color = color
        self.surf = image
        self.rect = self.surf.get_rect(topleft=(self.x, self.y))
