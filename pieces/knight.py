from steppable import Steppable

class Knight(Steppable):
    def __init__(self, color, board, pos):
        super(Knight, self).__init__(color, board, pos)

    def symbol(self):
        return u'\u2658' if self.color == "white" else u'\u265e'

    def _move_diffs(self):
        return [[-2, -1],
         [-1, -2],
         [-2, 1],
         [-1, 2],
         [1, -2],
         [2, -1],
         [1, 2],
         [2, 1]]
