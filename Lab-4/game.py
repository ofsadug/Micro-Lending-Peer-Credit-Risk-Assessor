from board import Board


class Game:
    def __init__(self):
        self.board = Board()
        self.best_score = 0
        self.history = []

    def display(self):
        print("\n" + "+------+------+------+------+")
        for row in self.board.grid:
            print(
                "|"
                + "|".join(
                    f"{x:^6}" if x else f"{' ':^6}" for x in row
                )
                + "|"
            )
            print("+------+------+------+------+")

        print("Score:", self.board.score, " Best:", self.best_score)

    def move(self, key):
        moves = {
            "a": (self.board.move_left, "left"),
            "d": (self.board.move_right, "right"),
            "w": (self.board.move_up, "up"),
            "s": (self.board.move_down, "down")
        }

        if key not in moves:
            return False

        old_grid = [row[:] for row in self.board.grid]
        old_score = self.board.score

        move_func, direction = moves[key]
        changed = move_func()

        if changed:
            # Save the state before this successful move.
            self.history = [(old_grid, old_score)]

            points = self.board.score - old_score

            # A new tile is added only after a successful move.
            self.board.add_random_tile()

            # Best score never decreases, including after undo.
            self.best_score = max(self.best_score, self.board.score)

            if self.board.last_move_merges:
                print(
                    f"Moved {direction}: "
                    f"{self.board.last_move_merges} merges, "
                    f"+{points} points"
                )
            else:
                print(f"Moved {direction}")
        else:
            print("No tiles moved.")

        return changed

    def undo(self):
        if not self.history:
            print("Nothing to undo.")
            return False

        old_grid, old_score = self.history.pop()

        self.board.grid = [row[:] for row in old_grid]
        self.board.score = old_score

        print("Move undone.")
        return True

    def run(self):
        print("2048 — W/A/S/D to move, U to undo, Q to quit.")

        while True:
            self.display()

            if any(2048 in row for row in self.board.grid):
                print("You reached 2048!")
                return

            if not self.board.can_move():
                print("No legal moves remain. Game over!")
                return

            key = input("> ").strip().lower()

            if key == "q":
                return

            if key == "u":
                self.undo()
                continue

            if key not in {"w", "a", "s", "d"}:
                print("Use W/A/S/D, U to undo, or Q to quit.")
                continue

            self.move(key)