# import pieces
from pieces import *
from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.rook import Rook
class Board(object):
    # LETTER_DICT = {
    #     0: 'a',
    #     1: 'b',
    #     2: 'c',
    #     3: 'd',
    #     4: 'e',
    #     5: 'f',
    #     6: 'g',
    #     7: 'h'
    # }

    LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8']

    def __init__(self):
        self.grid = [[None for x in range(8)] for x in range(8)]
        self.populate_board()

    def checkmate(self):
        return False

    def move(self, start, end_pos):
        pass

    def in_check(self, color):
        pass

    def fill_back_row(self, color):
        back_pieces = [
            Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook
        ]
        # r = Rook()
        i = 7 if color == "white" else 0
        for j, p in enumerate(back_pieces):
            p(color, self, [i, j])
        # pass

    def fill_pawn_row(self, color):
        i = 6 if color == "white" else 1
        for j in range(8):
            Pawn(color, self, [i, j])

    def populate_board(self):
        for color in ['white', 'black']:
            self.fill_back_row(color)
            self.fill_pawn_row(color)

    def render(self):
        self.__show_letters()
        for i1, row in enumerate(self.grid):
            print Board.NUMBERS[i1],
            for i2, el in enumerate(row):
                # str = el ? '_' : " %s" % el.symbol()
                str = " %s" % el.symbol() if el else ' _'
                print str,
            print Board.NUMBERS[i1]
        self.__show_letters()

    def add_piece(self, piece, pos):
        self.grid[pos[0]][pos[1]] = piece

    def __show_letters(self):
        print ' ',
        for i in range(8):
            print " %s" % Board.LETTERS[i],
        print
