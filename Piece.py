import pygame.image


class Piece:
    chess_pieces_images = {'black_bishop': 'img/pieces/black_bishop.png', 'black_king': 'img/pieces/black_king.png',
                           'black_knight': 'img/pieces/black_knight.png', 'black_pawn': 'img/pieces/black_pawn.png',
                           'black_queen': 'img/pieces/black_queen.png', 'black_rook': 'img/pieces/black_rook.png',
                           'white_bishop': 'img/pieces/white_bishop.png', 'white_king': 'img/pieces/white_king.png',
                           'white_knight': 'img/pieces/white_knight.png', 'white_pawn': 'img/pieces/white_pawn.png',
                           'white_queen': 'img/pieces/white_queen.png', 'white_rook': 'img/pieces/white_rook.png'}


    pieces = []

    def __init__(self, color: str, x: int, y: int, type: str):
        self.x = x
        self.y = y
        self.color = color
        self.first_move = True
        self.possible_move = []
        self.possible_attacks = []
        self.protected_pieces = []
        self.pos = (x, y)
        self.image = self.color + '_' + type
        self.surf = pygame.image.load(Piece.chess_pieces_images[self.image]).convert_alpha()
        self.rect = self.surf.get_rect(topleft=(x, y))




