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

    def __init__(self, fill_board = True):
        self.grid = [[None for x in range(8)] for x in range(8)]
        if fill_board:
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

    def try_move_piece(self, turn_color, from_pos, to_pos):
        print "position:", from_pos, to_pos
        piece = self.grid[from_pos[0]][from_pos[1]]
        # here i can also try using exception, but let's use true/false for the moment
        # print "piece color:", piece.color
        # print "turn_color:", turn_color
        # print piece.moves()
        if piece.color != turn_color:
            print "You must move your own piece."
            return False
        elif not to_pos in piece.moves():
            print "Piece does not move like that."
            return False
        elif not to_pos in piece.valid_moves():
            print "You cannot move into check"
            return False

        # self.grid[to_pos] = piece
        self.grid[to_pos[0]][to_pos[1]] = piece
        # self.grid[from_pos] = None
        self.grid[from_pos[0]][from_pos[1]] = None
        piece.pos = to_pos
        return True

    def move_piece(self, from_pos, to_pos):
        piece = self.grid[from_pos[0]][from_pos[1]]
        # self.grid[to_pos] = piece
        self.grid[to_pos[0]][to_pos[1]] = piece
        # self.grid[from_pos] = None
        self.grid[from_pos[0]][from_pos[1]] = None
        piece.pos = to_pos


    def is_valid_pos(self, pos):
        return all([(coord in range(8)) for coord in pos])

    def is_empty(self, pos):
        return self.grid[pos[0]][pos[1]] == None

    def dup(self):
        new_board = Board(False)

        for piece in self.pieces():
            type(piece)(piece.color, new_board, piece.pos)

        return new_board

    def pieces(self):
        return [piece for piece in [piece for row in self.grid for piece in row] if piece]

    def is_in_check(self, color):
        king_pos = self.__find_king(color).pos
        # for p in self.pieces():
        #     print p
        #     print p.moves()
        return any([(p.color != color and king_pos in p.moves()) for p in self.pieces()])

    def get_piece(self, pos):
        # may need to raise an exception
        i, j = pos
        return self.grid[i][j]

    def __find_king(self, color):
        for piece in self.pieces():
            # print type(piece)
            if piece.color == color and type(piece) is King:
                return piece

    def __show_letters(self):
        print ' ',
        for i in range(8):
            print " %s" % Board.LETTERS[i],
        print
