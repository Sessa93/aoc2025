
from src.day_6.problem_1 import Problem1Day6 as Problem


class TestProblem1Day6:
    def test_simple_case(self):
        input = """
        123 328  51 64 
        45 64  387 23 
        6 98  215 314
        *   +   *   + 
        """

        problem = Problem(input=input)
        answer = problem.answer()

        assert answer == 4277556
    
    def test_aoc_answer(self):
        problem = Problem()
        answer = problem.answer()

        assert answer == 5524274308182
