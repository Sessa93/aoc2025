from pathlib import Path
from typing import Any

from src.base.abstract_problem import AbstractProblem

from rich import print


class Problem2(AbstractProblem):
    def __init__(self, input=Path(__file__).parent / "data/input.txt"):
        super().__init__(name="Problem 2 Day 4", input=input)

    def get_input_from_string(self, input_string: str):
        ranges = []
        for line in list(map(str.strip, input_string.strip().split("\n"))):
            if "-" in line:
                a, b = line.split("-")
                ranges.append((int(a), int(b)))
            else:
                continue
        return ranges

    def get_input_from_file(self, file_path: str):
        with open(file_path, "r") as f:
            map = f.read().strip()
            return self.get_input_from_string(input_string=map)

    def answer(self) -> Any:
        ranges = self.input
        ranges.sort(key=lambda r: r[0])

        merged = []
        cur_start, cur_end = ranges[0]
        for start, end in ranges[1:]:
            # overlapping ranges
            if start <= cur_end + 1:
                cur_end = max(cur_end, end)
            # disjoint ranges
            else:
                merged.append((cur_start, cur_end))
                cur_start, cur_end = start, end
        merged.append((cur_start, cur_end))

        total = sum(end - start + 1 for start, end in merged)
        return total
