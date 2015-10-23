from board import Board
from player import HumanPlayer

class Game(object):
    def __init__(self):
        self.board = Board()
        # self.display = Display(self.board)
        self.players = {"white": HumanPlayer("white"), "black": HumanPlayer("black")}
        self.current_player = "white"

    def play(self):
        # print "Game starts!"
        while not self.board.checkmate():
            # raw_input("next step")
            from_pos, to_pos = self.players[self.current_player].make_move(self.board)
            board.move_piece(self.current_player, from_pos, to_pos)

            self.__swap_turn()
            # self.__notify_players()

        self.board.render()

    # def __notify_players():
    #     if board.is_in_check(self.current_player)

    def __swap_turn():
        # self.current_player = (current_player == "white") ? "black" : "white"
        self.current_player = "black" if current_player == "white" else "white"

if __name__ == "__main__":
    # print "Hello world!"
    Game().play()
