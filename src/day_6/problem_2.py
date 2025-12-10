import math
from typing import Any, List, Tuple

from src.base.abstract_problem import AbstractProblem


class Problem2Day6(AbstractProblem):
    def __init__(self, input=None):
        super().__init__(day=6, problem_number=2, input=input)

    def parse_input(self, input_string: str) -> List[Tuple[str, List[int]]]:
        lines = input_string.splitlines()
        while lines and not lines[0].strip():
            lines.pop(0)
        while lines and not lines[-1].strip():
            lines.pop()

        width = max(len(line) for line in lines)
        grid = [line.ljust(width) for line in lines]

        column_groups: List[List[List[str]]] = []
        current_group: List[List[str]] = []

        for col_idx in range(width):
            column = [grid[row_idx][col_idx] for row_idx in range(len(grid))]
            if all(ch == " " for ch in column):
                if current_group:
                    column_groups.append(current_group)
                    current_group = []
                continue
            current_group.append(column)

        if current_group:
            column_groups.append(current_group)

        return [self._columns_to_problem(group) for group in column_groups]

    @staticmethod
    def _columns_to_problem(columns: List[List[str]]) -> Tuple[str, List[int]]:
        operator = None
        numbers: List[int] = []

        for column in columns:
            digits = "".join(ch for ch in column[:-1] if ch != " ")
            if digits:
                numbers.append(int(digits))
            if operator is None and column[-1] != " ":
                operator = column[-1]

        numbers.reverse()
        return operator, numbers

    def answer(self) -> Any:
        total = 0
        for operator, numbers in self.input or []:
            if operator == "+":
                total += sum(numbers)
            elif operator == "*":
                total += math.prod(numbers)
            else:
                raise ValueError(f"Unsupported operator: {operator}")
        return total
