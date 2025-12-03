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
    def to_int(tuple_str):
        return int("".join(map(str, tuple_str)))

    @staticmethod
    def combs(k, n):
        p = [1]
        f = 1 << k
        for i in range(1, n):
            p.append((p[-1] * f) // i)
            f -= 1
        return p

    @staticmethod
    def get_max_from_bank(bank):
        int_bank = list(map(int, bank))
        max_val = 0
        for comb in itertools.combinations(int_bank, 12):
            int_comb = Problem2.to_int(comb)
            if int_comb > max_val:
                max_val = int_comb
        return max_val

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
