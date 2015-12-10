from slidable import Slidable

class Queen(Slidable):
    def __init__(self, color, board, pos):
        super(Queen, self).__init__(color, board, pos)

    def move_dirs(self):
        return self.horizontal_dirs() + self.diagonal_dirs()

    def symbol(self):
        return u'\u2655' if self.color == "white" else u'\u265b'
