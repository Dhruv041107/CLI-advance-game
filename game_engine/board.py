import json

class Board:
    def __init__(self, config_path):
        with open(config_path, "r") as f:
            data = json.load(f)
        self.size = data["size"]
        self.snakes = {int(k): v for k, v in data["snakes"].items()}
        self.ladders = {int(k): v for k, v in data["ladders"].items()}

    def apply_rules(self, position):
        if position in self.snakes:
            return self.snakes[position]
        if position in self.ladders:
            return self.ladders[position]
        return position
