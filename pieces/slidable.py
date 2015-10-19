class Slidable(Piece):
    def __init__(self):
        super(Piece, self).__init__(color, board, pos)
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


    def moves(self):
        moves = []
        for dx, dy in self.move_dirs:
            moves.concat(self.__grow_unblocked_moves_in_dir(dx, dy))

    def __grow_unblocked_moves_in_dir(dx, dy):
        cur_x, cur_y = pos
        moves = []

        while True:
            cur_x, cur_y = cur_x + dx, cur_y + dy
            pos = [cur_x, cur_y]
            if not self.board.is_valid_pos(pos):
                break

            if board.is_empty(pos):
                moves.append(pos)
            else:
                if self.board.get_piece(pos).color != color:
                    moves.append(pos)
                break
        return moves
