import os

class HumanPlayer(object):
    LETTER_DICT = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7
    }

    NUMBER_DICT = {
        '1': 0,
        '2': 1,
        '3': 2,
        '4': 3,
        '5': 4,
        '6': 5,
        '7': 6,
        '8': 7
    }

    def __init__(self, color):
        self.color = color

    def make_move(self, board):
        from_pos, to_pos = None, None

        while not(from_pos and to_pos):
            os.system('clear')
            board.render()

            # if from_pos:
            #     print "%s's turn. Move to where?" % self.color
            #     to_pos = raw_input()
            # else:
            #     print "%s's turn. Move from where?" % self.color
            #     from_pos = raw_input()
            print "Current player: %s" % self.color

            from_pos = self.__get_pos("from pos:")
            to_pos = self.__get_pos("to pos:")

        return [from_pos, to_pos]

    def __get_pos(self, prompt):
        print prompt
        # test if the input is valid
        pos = raw_input()
        # see if length of pos is 2 and if letter and nuber is valid
        while not self.__valid(pos):
            pos = raw_input()

        # return pos
        return [HumanPlayer.NUMBER_DICT[pos[1]], HumanPlayer.LETTER_DICT[pos[0]]]

    def __valid(self, pos):
        if len(pos) != 2:
            return False
        if not pos[0] in 'abcdefgh':
            return False
        if not int(pos[1]) in range(1, 9):
            return False
        return True
