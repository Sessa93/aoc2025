from typing import Any

from src.base.abstract_problem import AbstractProblem


class Problem1Day5(AbstractProblem):
    def __init__(self, input=None):
        super().__init__(day=5, problem_number=1, input=input)

    def parse_input(self, input_string: str):
        ranges = []
        ingredients = []
        for line in list(map(str.strip, input_string.strip().split("\n"))):
            if "-" in line:
                a, b = line.split("-")
                ranges.append((int(a), int(b)))
            elif line == "":
                continue
            else:
                ingredients.append(int(line))
        return ingredients, ranges

    def answer(self) -> Any:
        ingredients, ranges = self.input
        fresh_ingredient_count = 0
        for ingredient in ingredients:
            for r in ranges:
                if r[0] <= ingredient <= r[1]:
                    fresh_ingredient_count += 1
                    break
        return fresh_ingredient_count
