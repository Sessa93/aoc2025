from src.day_1.problem_1 import ProblemDay1


class TestProblem1Day1:
    def test_simple_rotation(self):
        problem = ProblemDay1(input="R1000")

        answer = problem.answer()

        assert answer == 0

    def test_simple_more_complicated_rotation(self):
        problem = ProblemDay1(
            input="""
                                    L68
                                    L30
                                    R48
                                    L5
                                    R60
                                    L55
                                    L1
                                    L99
                                    R14
                                    L82
                                    """
        )

        answer = problem.answer()

        assert answer == 3

    def test_aoc_answer(self):
        problem = ProblemDay1()

        answer = problem.answer()

        assert answer == 1084
