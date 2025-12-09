from concurrent.futures import ThreadPoolExecutor
from typing import Any

from src.base.abstract_problem import AbstractProblem


class Problem2Day3(AbstractProblem):
    def __init__(self, input=None):
        super().__init__(day=3, problem_number=2, input=input)

    def parse_input(self, input_string: str):
        return list(map(str.strip, input_string.strip().split("\n")))

    @staticmethod
    def get_max_from_bank(bank):
        to_remove = len(bank) - 12
        stack = []

        for digit in bank:
            while to_remove and stack and stack[-1] < digit:
                stack.pop()
                to_remove -= 1
            stack.append(digit)
        result_digits = stack[:12]
        return int("".join(result_digits))

    def answer(self) -> Any:
        with ThreadPoolExecutor() as executor:
            results = list(executor.map(self.get_max_from_bank, self.input))
        return sum(results)
