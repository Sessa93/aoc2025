from collections import defaultdict
from typing import Any, List, Optional, Tuple

from src.base.abstract_problem import AbstractProblem


class Problem2Day7(AbstractProblem):
    def __init__(self, input=None):
        super().__init__(day=7, problem_number=2, input=input)

    def parse_input(
        self, input_string: str
    ) -> Tuple[List[str], Optional[Tuple[int, int]]]:
        stripped = input_string.strip("\n")
        lines = [line.rstrip("\n") for line in stripped.splitlines() if line.strip()]
        width = max(len(line) for line in lines)
        grid: List[str] = []
        start: Optional[Tuple[int, int]] = None

        for row, raw_line in enumerate(lines):
            line = raw_line.ljust(width, ".")
            if "S" in line:
                start = (row, line.index("S"))
            grid.append(line)

        return grid, start

    def answer(self) -> Any:
        grid, start = self.input
        rows = len(grid)
        cols = len(grid[0])
        start_row, start_col = start

        active = {start_col: 1}
        for row in range(start_row + 1, rows):
            next_active = defaultdict(int)
            for col, count in active.items():
                if count == 0 or not (0 <= col < cols):
                    continue
                cell = grid[row][col]
                if cell == "^":
                    if col - 1 >= 0:
                        next_active[col - 1] += count
                    if col + 1 < cols:
                        next_active[col + 1] += count
                else:
                    next_active[col] += count
            active = next_active
            if not active:
                break

        return sum(active.values())
