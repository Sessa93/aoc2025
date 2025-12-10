from collections import deque
from typing import Any, List, Optional, Tuple

from src.base.abstract_problem import AbstractProblem


class Problem1Day7(AbstractProblem):
    def __init__(self, input=None):
        super().__init__(day=7, problem_number=1, input=input)

    def parse_input(self, input_string: str) -> Tuple[List[str], Optional[Tuple[int, int]]]:
        stripped = input_string.strip("\n")
        lines = stripped.splitlines()
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
        parsed = self.input

        grid, start = parsed

        rows = len(grid)
        cols = len(grid[0])
        start_row, start_col = start
        if start_row + 1 >= rows:
            return 0

        active_cols = {start_col}
        splits = 0

        for row in range(start_row + 1, rows):
            if not active_cols:
                break

            queue = deque(active_cols)
            processed_cols = set()
            next_cols = set()

            while queue:
                col = queue.popleft()
                if col in processed_cols or not (0 <= col < cols):
                    continue
                processed_cols.add(col)

                cell = grid[row][col]
                if cell == "^":
                    splits += 1
                    if col - 1 >= 0:
                        queue.append(col - 1)
                    if col + 1 < cols:
                        queue.append(col + 1)
                else:
                    next_cols.add(col)

            active_cols = next_cols

        return splits


