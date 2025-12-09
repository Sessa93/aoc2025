from src.base.abstract_problem import AbstractProblem


class Problem2Day2(AbstractProblem):
    def __init__(self, input=None):
        super().__init__(day=2, problem_number=2, input=input)

    def parse_input(self, input_string: str):
        return [
            range(int(start), int(end) + 1)
            for start, end in (part.split("-") for part in input_string.split(","))
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
