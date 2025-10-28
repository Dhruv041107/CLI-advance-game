class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.position = 0

    def move(self, steps):
        self.position += steps

    def set_position(self, pos):
        self.position = pos
