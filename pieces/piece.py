class Piece(object):
    def __init__(self, color, board, pos):
        self.color, self.board, self.pos = color, board, pos
        self.board.add_piece(self, pos)

    def valid_moves(self):
        return [to_pos for to_pos in self.moves() if not self.__move_into_check(to_pos)]

    def __move_into_check(self, to_pos):
        test_board = self.board.dup()
        test_board.move_piece(self.pos, to_pos)
        return test_board.is_in_check(self.color)

    def moves(self):
        return []
