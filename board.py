class Board(object):

    def __init__(self):
        self.grid = [[none for x in range(5)] for x in range(5)]
        populate_board

    def checkmate(self):
        return False

    def move(self, start, end_pos):
        pass

    def in_check(self, color):
        pass

    def fill_back_row(self, color):
        pass

    def fill_pawn_row(self, color):
        pass

    def populate_board(self):
        for color in ['white', 'black']:
            fill_back_row(color)
            fill_pawn_row(color)
