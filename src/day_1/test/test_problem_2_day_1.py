from src.day_1.problem_2 import ProblemDay2


class TestProblem2Day1:
    def test_simple_rotation(self):
        problem = ProblemDay2(input="R1000")

        answer = problem.answer()

        assert answer == 10

    def test_simple_more_complicated_rotation(self):
        problem = ProblemDay2(
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

        assert answer == 6

    def test_aoc_answer(self):
        problem = ProblemDay2()

        answer = problem.answer()

        assert answer == 6475
