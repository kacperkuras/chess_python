import pygame
from BoardSquare import BoardSquare
from Network import Network
from Scene import Scene
from Button import Button
from King import King
from Queen import Queen
from Pawn import Pawn
from Rook import Rook
from Knight import Knight
from Bishop import Bishop

class Game:
    def __init__(self):
        self.turn = 'white'
        self.you = 'white'
        self.enemy = 'black'
        self.fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq'
        self.BOARD_HEIGHT = 768
        self.BOARD_WIDTH = 768
        self.BOARD_SQUARE_SIZE = 96


