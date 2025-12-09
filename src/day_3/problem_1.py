import itertools
from typing import Any

from src.base.abstract_problem import AbstractProblem


class Problem1Day3(AbstractProblem):
    def __init__(self, input=None):
        super().__init__(day=3, problem_number=1, input=input)

    def parse_input(self, input_string: str):
        return list(map(str.strip, input_string.strip().split("\n")))

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
