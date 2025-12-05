from src.day_5.problem_2 import Problem2


class TestProblem2Day5:
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

        problem = Problem2(input=input)
        answer = problem.answer()

        assert answer == 14

    def test_aoc_answer(self):
        problem = Problem2()
        answer = problem.answer()

        assert answer == 357608232770687
