
from src.day_8.problem_1 import Problem1Day8 as Problem


class TestProblem1Day8:
    def test_simple_case(self):
        input = ""

        problem = Problem(input=input)
        answer = problem.answer()

        assert answer == 42
    
    def test_aoc_answer(self):
        problem = Problem()
        answer = problem.answer()

        assert answer == 42
