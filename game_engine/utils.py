from collections import deque

class History:
    def __init__(self):
        self.stack = deque()
        self.redo_stack = deque()

    def append(self, cmd):
        self.stack.append(cmd)
        self.redo_stack.clear()

    def undo(self):
        if self.stack:
            cmd = self.stack.pop()
            cmd.undo()
            self.redo_stack.append(cmd)

    def redo(self):
        if self.redo_stack:
            cmd = self.redo_stack.pop()
            cmd.execute()
            self.stack.append(cmd)
