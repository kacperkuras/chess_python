from Piece import Piece


class Rook(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y, 'rook')
