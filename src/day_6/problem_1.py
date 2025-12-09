
from typing import Any

from src.base.abstract_problem import AbstractProblem


class Problem1Day6(AbstractProblem):
    def __init__(self, input=None):
        super().__init__(day=6, problem_number=1, input=input)
    
    def parse_input(self, input_string: str):
        raise NotImplementedError()
    
    def answer(self) -> Any:
        raise NotImplementedError()
