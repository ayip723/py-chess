from board import Board

class Game(object):
    def __init__(self):
        self.board = Board()
        self.display = Display(self.board)

    def play(self):
        # print "Game starts!"
        while not self.board.checkmate():
            raw_input("next step")
        # pass

    def _notify_players():
        pass

    def swap_turn():
        pass

if __name__ == "__main__":
    # print "Hello world!"
    Game().play()
