from piece import Piece

class Steppable(Piece):
    def __init__(self, color, board, pos):
        super(Steppable, self).__init__(color, board, pos)

    def moves(self):
        moves = []
        for dx, dy in self._move_diffs():
            cur_x, cur_y = self.pos
            pos = [cur_x + dx, cur_y + dy]

            if not self.board.is_valid_pos(pos): continue

            if self.board.is_empty(pos):
                moves.append(pos)
            elif self.board.get_piece(pos).color != self.color:
                moves.append(pos)
        return moves

    def _move_diffs(self):
        pass
