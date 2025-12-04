from pathlib import Path
from typing import Any
from rich import print

from src.base.abstract_problem import AbstractProblem


class Problem2(AbstractProblem):
    def __init__(self, input=Path(__file__).parent / "data/input.txt"):
        super().__init__(name="Problem 2 Day 4", input=input)

    def get_input_from_string(self, input_string: str):
        return list(map(str.strip, input_string.strip().split("\n")))

    def get_input_from_file(self, file_path: str):
        with open(file_path, "r") as f:
            map = f.read().strip()
            return self.get_input_from_string(input_string=map)

    @staticmethod
    def _neighbors(r: int, c: int, rows: int, cols: int):
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    yield nr, nc

    def answer(self) -> Any:
        grid = [list(row) for row in self.input]
        rows, cols = len(grid), len(grid[0]) if grid else 0

        total_removed = 0
        while True:
            to_remove = []

            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] != "@":
                        continue
                    neighbor_rolls = 0
                    for nr, nc in self._neighbors(r, c, rows, cols):
                        if grid[nr][nc] == "@":
                            neighbor_rolls += 1

                    if neighbor_rolls < 4:
                        to_remove.append((r, c))

            if not to_remove:
                break

            for r, c in to_remove:
                grid[r][c] = "."
            total_removed += len(to_remove)
            print(f"Removed {len(to_remove)} cells, total removed: {total_removed}")

        return total_removed
