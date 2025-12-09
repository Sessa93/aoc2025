from typing import Any

from src.base.abstract_problem import AbstractProblem


class Problem2Day5(AbstractProblem):
    def __init__(self, input=None):
        super().__init__(day=5, problem_number=2, input=input)

    def parse_input(self, input_string: str):
        ranges = []
        for line in list(map(str.strip, input_string.strip().split("\n"))):
            if "-" in line:
                a, b = line.split("-")
                ranges.append((int(a), int(b)))
            else:
                continue
        return ranges

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
