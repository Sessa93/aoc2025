from pathlib import Path
from typing import Any

from src.base.abstract_problem import AbstractProblem


class Problem1(AbstractProblem):
    def __init__(self, input=Path(__file__).parent / "data/input.txt"):
        super().__init__(name="Problem 1 Day 4", input=input)

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
        grid = self.input
        rows = len(grid)
        cols = len(grid[0]) if rows else 0

        accessible = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "@":
                    continue
                adj_rolls = sum(
                    1
                    for nr, nc in self._neighbors(r, c, rows, cols)
                    if grid[nr][nc] == "@"
                )
                if adj_rolls < 4:
                    accessible += 1

        return accessible
