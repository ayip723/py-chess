from piece import Piece

class Slidable(Piece):
    def __init__(self, color, board, pos):
        super(Slidable, self).__init__(color, board, pos)
        # pass

    HORIZONTAL_DIRS = [
        [-1, 0],
        [0, -1],
        [0, 1],
        [1, 0]
    ]

    DIAGONAL_DIRS = [
        [-1, -1],
        [-1, 1],
        [1, -1],
        [1, 1]
    ]

    def horizontal_dirs(self):
        return Slidable.HORIZONTAL_DIRS

    def diagonal_dirs(self):
        return Slidable.DIAGONAL_DIRS

    def moves(self):
        moves = []
        for dx, dy in self.move_dirs():
            moves += (self.__grow_unblocked_moves_in_dir(dx, dy))
        return moves

    def __grow_unblocked_moves_in_dir(self, dx, dy):
        cur_x, cur_y = self.pos
        moves = []

        while True:
            cur_x, cur_y = cur_x + dx, cur_y + dy
            pos = [cur_x, cur_y]
            if not self.board.is_valid_pos(pos):
                break

            if self.board.is_empty(pos):
                moves.append(pos)
            else:
                if self.board.get_piece(pos).color != self.color:
                    moves.append(pos)
                break
        return moves
