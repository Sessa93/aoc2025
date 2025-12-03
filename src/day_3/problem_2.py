import itertools
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

from src.base.abstract_problem import AbstractProblem


class Problem2(AbstractProblem):
    def __init__(self, input=Path(__file__).parent / "data/input.txt"):
        super().__init__(name="Problem 1 Day 3", input=input)

    def get_input_from_string(self, input_string: str):
        return list(map(str.strip, input_string.strip().split('\n')))

    def get_input_from_file(self, file_path: str):
        with open(file_path, "r") as f:
            banks = f.read().strip()
            return self.get_input_from_string(input_string=banks)

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

if __name__ == "__main__":
    input = """
        987654321111111
        811111111111119
        234234234234278
        818181911112111
    """

    problem = Problem2()
    answer = problem.answer()
    print(answer)
