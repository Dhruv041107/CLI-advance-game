class Command:
    def execute(self):
        pass
    def undo(self):
        pass


class MoveCommand(Command):
    def __init__(self, player, board, steps):
        self.player = player
        self.board = board
        self.steps = steps
        self.prev_pos = player.position
        self.new_pos = None

    def execute(self):
        self.player.move(self.steps)
        if self.player.position > self.board.size:
            self.player.set_position(self.prev_pos)
        else:
            self.player.set_position(self.board.apply_rules(self.player.position))
        self.new_pos = self.player.position

    def undo(self):
        self.player.set_position(self.prev_pos)
