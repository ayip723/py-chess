from piece import Piece

class Pawn(Piece):
    def __init__(self, color, board, pos):
        super(Pawn, self).__init__(color, board, pos)

    def moves(self):
        # print self.forward_steps() + self.side_attacks()
        return self.forward_steps() + self.side_attacks()

    def forward_dir(self):
        return -1 if self.color == "white" else 1

    def forward_steps(self):
        i, j = self.pos
        one_step = [i + self.forward_dir(), j]
        if not self.board.is_valid_pos(one_step) and board.is_empty(one_step):
            return []

        steps = [one_step]
        two_step = [i + 2 * self.forward_dir(), j]
        if self.__is_at_start_row() and self.board.is_empty(two_step):
            steps.append(two_step)
        return steps

    def side_attacks(self):
        i, j = self.pos
        side_moves = [[i + self.forward_dir(), j - 1], [i + self.forward_dir(), j + 1]]
        return [pos for pos in side_moves if self.__vaild_side_move(pos)]

    def __vaild_side_move(self, pos):
        if not self.board.is_valid_pos(pos):
            return False
        if self.board.is_empty(pos):
            return False
        threatened_piece = self.board.get_piece(pos)
        return threatened_piece and threatened_piece.color != self.color

    def side_steps(self):
        pass

    def __is_at_start_row(self):
        return pos[0] == 6 if self.color == "WHITE" else 1

    def symbol(self):
        return u'\u2659' if self.color == "white" else u'\u265f'
