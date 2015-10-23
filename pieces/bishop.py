from slidable import Slidable
# import Slidable

class Bishop(Slidable):
    def __init__(self, color, board, pos):
        super(Bishop, self).__init__(color, board, pos)

    def symbol(self):
        return u'\u265d' if self.color == "white" else u'\u2657'
