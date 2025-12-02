from pathlib import Path
from typing import Any

from src.base.abstract_problem import AbstractProblem


class Problem1(AbstractProblem):
    def __init__(self, input=Path(__file__).parent / "data/input.txt"):
        super().__init__(name="Problem 1 Day 2", input=input)

    def get_input_from_string(self, input_string: str):
        return [
            range(int(start), int(end) + 1)
            for start, end in (part.split("-") for part in input_string.split(","))
        ]

    def get_input_from_file(self, file_path: str):
        with open(file_path, "r") as f:
            ranges_string = f.read().strip()
            return [
                range(int(start), int(end) + 1)
                for start, end in (part.split("-") for part in ranges_string.split(","))
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
