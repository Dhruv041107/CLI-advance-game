from game_engine.board import Board
from game_engine.player import Player
from game_engine.ui import UI
from game_engine.states import MenuState
from game_engine.utils import History

class Game:
    def __init__(self):
        self.ui = UI()
        self.board = Board("config/board.json")
        self.players = [
            Player("You", "yellow"),
            Player("Computer", "magenta")
        ]
        self.state = MenuState()
        self.history = History()
        self.running = True

    def change_state(self, new_state):
        self.state = new_state

    def replay(self):
        self.ui.show_message("Replaying last game...", "bold yellow")
        for cmd in self.history.stack:
            cmd.execute()
            self.ui.draw_board(self.board, self.players)

    def run(self):
        while self.running:
            self.state.handle(self)

if __name__ == "__main__":
    Game().run()
