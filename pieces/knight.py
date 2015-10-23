from slidable import Slidable

class Knight(Slidable):
    def __init__(self, color, board, pos):
        super(Knight, self).__init__(color, board, pos)

    def move_dirs(self):
        return self.horizontal_dirs + self.diagonal_dirs

    def symbol(self):
        return u'\u2658' if self.color == "white" else u'\u265e'
