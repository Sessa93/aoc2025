from pathlib import Path

from src.base.abstract_problem import AbstractProblem


class Problem2(AbstractProblem):
    def __init__(self, input=Path(__file__).parent / "data/input.txt"):
        super().__init__(name="Problem 2 Day 2", input=input)

    def get_input_from_string(self, input_string: str):
        return [
            range(int(start), int(end) + 1)
            for start, end in (part.split("-") for part in input_string.split(","))
        ]

    def get_input_from_file(self, file_path: str):
        with open(file_path, "r") as f:
            ranges_string = f.read().strip()
            return [
                range(int(start), int(end) + 1)
                for start, end in (part.split("-") for part in ranges_string.split(","))
            ]

    @staticmethod
    def is_valid_id(id: int) -> bool:
        input_id = str(id)
        n = len(input_id)

        for pattern_len in range(1, n // 2 + 1):
            if n % pattern_len != 0:
                continue
            pattern = input_id[:pattern_len]
            if pattern * (n // pattern_len) == input_id:
                return False

        return True

    def answer(self):
        total_sum = 0
        for r in self.input:
            for i in r:
                if not self.is_valid_id(i):
                    total_sum += i
        return total_sum
