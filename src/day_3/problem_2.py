from pathlib import Path
from typing import Any

from src.base.abstract_problem import AbstractProblem


class Problem2(AbstractProblem):
    def __init__(self, input=Path(__file__).parent / "data/input.txt"):
        super().__init__(name="Problem 2 Day 3", input=input)

    def get_input_from_string(self, input_string: str):
        pass

    def get_input_from_file(self, file_path: str):
        with open(file_path, "r") as f:
            pass

    def answer(self) -> Any:
        pass
