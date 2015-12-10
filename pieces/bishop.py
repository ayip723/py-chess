from slidable import Slidable
# import Slidable

class Bishop(Slidable):
    def __init__(self, color, board, pos):
        super(Bishop, self).__init__(color, board, pos)

    def symbol(self):
        return u'\u2657' if self.color == "white" else u'\u265d'

    def move_dirs(self):
        return self.diagonal_dirs()
