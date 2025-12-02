import enum
from pathlib import Path
from typing import Any

from src.base.abstract_problem import AbstractProblem


class RotationDirection(enum.Enum):
    L = "L"
    R = "R"


class ProblemDay1(AbstractProblem):
    INITIAL_POSITION = 50
    POSITION_AT_ZERO = 0
    MAX_POSITION = 100

    def __init__(self, input=Path(__file__).parent / "data/input.txt"):
        super().__init__(name="Problem 1 Day 1", input=input)

    def get_input_from_file(
        self, file_path="./data/input.txt"
    ) -> list[tuple[RotationDirection, int]]:
        with open(file_path, "r") as file:
            return [
                (RotationDirection(line[0]), int(line[1:]))
                for line in file.readlines()
                if len(line) > 0
            ]

    def get_input_from_string(
        self, input_string: str
    ) -> list[tuple[RotationDirection, int]]:
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


if __name__ == "__main__":
    print(ProblemDay1())
