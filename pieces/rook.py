from slidable import Slidable

class Rook(Slidable):
    def __init__(self, color, board, pos):
        super(Rook, self).__init__(color, board, pos)

    def move_dirs(self):
        return self.horizontal_dirs()

    def symbol(self):
        return u'\u2656' if self.color == "white" else u'\u265c'
