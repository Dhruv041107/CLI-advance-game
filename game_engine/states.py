from .commands import MoveCommand

class GameState:
    def handle(self, game): pass

class MenuState(GameState):
    def handle(self, game):
        from rich.prompt import Prompt
        choice = Prompt.ask("🎮 Start Game?", choices=["yes", "no"], default="yes")
        if choice == "yes":
            game.change_state(PlayingState())
        else:
            game.running = False

class PlayingState(GameState):
    def handle(self, game):
        ui = game.ui
        ui.draw_board(game.board, game.players)

        for player in game.players:
            input(f"\nPress Enter for {player.name}'s turn...")
            roll = ui.roll_dice(player)
            cmd = MoveCommand(player, game.board, roll)
            cmd.execute()
            game.history.append(cmd)
            ui.draw_board(game.board, game.players)

            if player.position == game.board.size:
                ui.show_message(f"🏆 {player.name} wins!", "bold green")
                game.change_state(GameOverState())
                return

class GameOverState(GameState):
    def handle(self, game):
        from rich.prompt import Prompt
        choice = Prompt.ask("🔁 Replay last game?", choices=["yes", "no"], default="no")
        if choice == "yes":
            game.replay()
        game.running = False
