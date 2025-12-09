from typing import Any

from src.base.abstract_problem import AbstractProblem


class Problem1Day2(AbstractProblem):
    def __init__(self, input=None):
        super().__init__(day=2, problem_number=1, input=input)

    def parse_input(self, input_string: str):
        return [
            range(int(start), int(end) + 1)
            for start, end in (part.split("-") for part in input_string.split(","))
        ]

    @staticmethod
    def is_valid_id(id: int) -> bool:
        input_id = str(id)
        if len(input_id) % 2 != 0:
            return True

        mid = len(input_id) // 2
        first_half = input_id[:mid]
        second_half = input_id[mid:]

        return not first_half == second_half

    def answer(self) -> Any:
        total_sum = 0
        for r in self.input:
            for i in r:
                if not self.is_valid_id(i):
                    total_sum += i
        return total_sum
