import enum
from typing import Any

from src.base.abstract_problem import AbstractProblem


class RotationDirection(enum.Enum):
    L = "L"
    R = "R"


class Problem1Day1(AbstractProblem):
    INITIAL_POSITION = 50
    POSITION_AT_ZERO = 0
    MAX_POSITION = 100

    def __init__(self, input=None):
        super().__init__(day=1, problem_number=1, input=input)

    def parse_input(self, input_string: str) -> list[tuple[RotationDirection, int]]:
        return [
            (RotationDirection(line.strip()[0]), int(line.strip()[1:]))
            for line in input_string.strip().split("\n")
            if len(line.strip()) > 0
        ]

    def answer(self) -> Any:
        position = self.INITIAL_POSITION
        password = 0
        for direction, degrees in self.input:
            if direction == RotationDirection.L:
                position -= degrees
            elif direction == RotationDirection.R:
                position += degrees
            position %= self.MAX_POSITION
            if position == 0:
                password += 1
        return password
