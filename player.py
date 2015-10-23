class HumanPlayer(object):
    def __init__(self, color):
        self.color = color

    def make_move(self, board):
        from_pos, to_pos = None, None

        while not(from_pos and to_pos):
            board.render()

            if from_pos:
                print "%s's turn. Move to where?" % self.color
                to_pos = raw_input()
            else:
                print "%s's turn. Move from where?" % self.color
                from_pos = raw_input()

        return [from_pos, to_pos]
