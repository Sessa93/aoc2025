import itertools
from pathlib import Path
from typing import Any

from base.abstract_problem import AbstractProblem


class Problem1(AbstractProblem):
    def __init__(self, input=Path(__file__).parent / "data/input.txt"):
        super().__init__(name="Problem 1 Day 3", input=input)

    def get_input_from_string(self, input_string: str):
        return list(map(str.strip, input_string.strip().split("\n")))

    def get_input_from_file(self, file_path: str):
        with open(file_path, "r") as f:
            banks = f.read().strip()
            return self.get_input_from_string(input_string=banks)

    @staticmethod
    def to_int(tuple_str):
        return int(tuple_str[0]) * 10 + int(tuple_str[1])

    def answer(self) -> Any:
        return sum(
            [
                max(list(map(self.to_int, list(itertools.combinations(bank, 2)))))
                for bank in self.input
            ]
        )
