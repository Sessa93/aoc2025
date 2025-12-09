import enum
from typing import Tuple, Any

from src.base.abstract_problem import AbstractProblem

INITIAL_POSITION = 50
PASSWORD = 0
MAX_POSITION = 100


class RotationDirection(enum.Enum):
    L = "L"
    R = "R"


class Problem2Day1(AbstractProblem):
    def __init__(self, input=None):
        super().__init__(day=1, problem_number=2, input=input)

    def parse_input(self, input_string: str) -> list[tuple[RotationDirection, int]]:
        return [
            (RotationDirection(line.strip()[0]), int(line.strip()[1:]))
            for line in input_string.strip().split("\n")
            if len(line.strip()) > 0
        ]

    @staticmethod
    def update_position(start_position, degrees) -> Tuple[int, int]:
        full_rotations = abs(degrees) // MAX_POSITION
        abs_degrees = abs(degrees) % MAX_POSITION

        if degrees > 0:
            partial_rotations = (
                1 if abs_degrees >= (MAX_POSITION - start_position) else 0
            )
        else:
            partial_rotations = 1 if abs_degrees >= start_position else 0

        if start_position == 0:
            partial_rotations = 0

        return full_rotations + partial_rotations, (
            start_position + degrees
        ) % MAX_POSITION

    def answer(self) -> Any:
        position = INITIAL_POSITION
        password = 0
        for direction, degrees in self.input:
            if direction == RotationDirection.L:
                degrees = -degrees
            passes, end_position = self.update_position(
                start_position=position, degrees=degrees
            )
            password += passes
            position = end_position
        return password
