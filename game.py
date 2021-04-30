from board import Board
from player import HumanPlayer

class Game(object):
    def __init__(self):
        self.board = Board()
        self.players = {"white": HumanPlayer("white"), "black": HumanPlayer("black")}
        self.current_player = "white"

    def play(self):
        while not self.board.checkmate():
            from_pos, to_pos = self.players[self.current_player].make_move(self.board)
            if not self.board.try_move_piece(self.current_player, from_pos, to_pos):
                continue

            self.__swap_turn()

        self.board.render()


    def __swap_turn(self):
        self.current_player = "black" if self.current_player == "white" else "white"

if __name__ == "__main__":
    Game().play()
