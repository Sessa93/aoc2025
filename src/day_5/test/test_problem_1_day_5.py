from src.day_5.problem_1 import Problem1


class TestProblem1Day5:
    def test_simple_case(self):
        input = """
            3-5
            10-14
            16-20
            12-18

            1
            5
            8
            11
            17
            32
        """

        problem = Problem1(input=input)
        answer = problem.answer()

        assert answer == 3

    def test_aoc_answer(self):
        problem = Problem1()
        answer = problem.answer()

        assert answer == 720