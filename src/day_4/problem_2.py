from typing import Any
from rich import print

from src.base.abstract_problem import AbstractProblem


class Problem2Day4(AbstractProblem):
    def __init__(self, input=None):
        super().__init__(day=4, problem_number=2, input=input)

    def parse_input(self, input_string: str):
        return list(map(str.strip, input_string.strip().split("\n")))

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
