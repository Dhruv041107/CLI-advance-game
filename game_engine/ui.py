from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import track
import time

console = Console()

class UI:
    def draw_board(self, board, players):
        table = Table(show_header=False, box=None)
        cells = []
        for i in range(board.size, 0, -1):
            text = str(i)
            for p in players:
                if p.position == i:
                    text = f"[{p.color}]●[/]"
            if i in board.snakes:
                text = f"[red]S↓[/]"
            elif i in board.ladders:
                text = f"[green]L↑[/]"
            cells.append(text)

        for i in range(0, board.size, 10):
            row = cells[i:i+10]
            if (i // 10) % 2 == 1:
                row.reverse()
            table.add_row(*row)
        console.clear()
        console.print(Panel(table, title="🎲 Snakes and Ladders 🎲", border_style="bold blue"))

    def roll_dice(self, player):
        for _ in track(range(10), description=f"{player.name} rolling..."):
            time.sleep(0.05)
        from random import randint
        roll = randint(1, 6)
        console.print(f"[{player.color}]🎲 {player.name} rolled a {roll}![/]")
        return roll

    def show_message(self, text, style="bold cyan"):
        console.print(text, style=style)
