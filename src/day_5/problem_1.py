from pathlib import Path
from typing import Any

from rich import print

from src.base.abstract_problem import AbstractProblem


class Problem1(AbstractProblem):
    def __init__(self, input=Path(__file__).parent / "data/input.txt"):
        super().__init__(name="Problem 1 Day 5", input=input)

    def get_input_from_string(self, input_string: str):
        ranges = []
        ingredients = []
        for line in list(map(str.strip, input_string.strip().split("\n"))):
            if '-' in line:
                a, b = line.split('-')
                ranges.append((int(a), int(b)))
            elif line == "":
                continue
            else:
                ingredients.append(int(line))
        return ingredients, ranges

    def get_input_from_file(self, file_path: str):
        with open(file_path, "r") as f:
            map = f.read().strip()
            return self.get_input_from_string(input_string=map)

    def answer(self) -> Any:
        ingredients, ranges = self.input
        fresh_ingredient_count = 0
        for ingredient in ingredients:
            for r in ranges:
                if r[0] <= ingredient <= r[1]:
                    fresh_ingredient_count += 1
                    break
        return fresh_ingredient_count

if __name__ == "__main__":
    input = """
        3-5
        10-14
        16-20
        12-18
        
        1
        5
        8
        11
        17
        32
    """
    problem = Problem1()
    print(problem.answer())
