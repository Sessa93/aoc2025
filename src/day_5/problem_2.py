from src.base.abstract_problem import AbstractProblem

from rich import print

class Problem2(AbstractProblem):
    def __init__(self, input=Path(__file__).parent / "data/input.txt"):
        super().__init__(name="Problem 2 Day 4", input=input)

    def get_input_from_string(self, input_string: str):
        return list(map(str.strip, input_string.strip().split("\n")))

    def get_input_from_file(self, file_path: str):
        with open(file_path, "r") as f:
            map = f.read().strip()
            return self.get_input_from_string(input_string=map)