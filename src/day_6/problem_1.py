import math
from typing import Any
from rich import print
from src.base.abstract_problem import AbstractProblem


class Problem1Day6(AbstractProblem):
    def __init__(self, input=None):
        super().__init__(day=6, problem_number=1, input=input)
    
    def parse_input(self, input_string: str):
        numbers = []
        ops = []
        for line in list(map(str.strip, input_string.strip().split("\n"))):
            if line.startswith("*") or line.startswith("+"):
                ops = " ".join(line.split()).split(" ")
            else:
                numbers.append(list(map(int, " ".join(line.split()).split(" "))))
        return numbers, ops

    def answer(self) -> Any:
        numbers, ops = self.input
        transposed_numbers = [list(row) for row in zip(*numbers)]
        total = 0
        for i, op in enumerate(ops):
            if op == "*":
                total += math.prod(transposed_numbers[i])
            elif op == "+":
                total += sum(transposed_numbers[i])
            else:
                continue
        return total