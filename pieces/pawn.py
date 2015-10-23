from piece import Piece

class Pawn(Piece):
    def __init__(self, color, board, pos):
        super(Pawn, self).__init__(color, board, pos)

    def moves(self):
        self.forward_steps + side_attacks

    def __is_at_start_row(self):
        return pos[0] == 6 if self.color == "WHITE" else 1

    def symbol(self):
        return u'\u2659' if self.color == "white" else u'\u265f'
