from piece import Piece

class Steppable(Piece):
    def __init__(self, color, board, pos):
        super(Steppable, self).__init__(color, board, pos)

    def moves(self):
        moves = []
        for dx, dy in move_diffs:
            cur_x, cur_y = pos
            pos = [cur_x + dx, cur_y + dy]

            if not self.board.is_valid_pos(pos): continue

            if self.board.is_empty(pos):
                moves.append(pos)
            elif self.board.get_piece(pos).color != self.color:
                moves << pos
        return moves

    def __move_diffs(self):
        pass
