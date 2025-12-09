from src.day_4.problem_2 import Problem2Day4 as Problem


class TestProblem2Day4:
    def test_simple_case(self):
        input = """
            ..@@.@@@@.
            @@@.@.@.@@
            @@@@@.@.@@
            @.@@@@..@.
            @@.@@@@.@@
            .@@@@@@@.@
            .@.@.@.@@@
            @.@@@.@@@@
            .@@@@@@@@.
            @.@.@@@.@.
        """

        problem = Problem(input=input)
        answer = problem.answer()

        assert answer == 43

    def test_aoc_answer(self):
        problem = Problem()
        answer = problem.answer()

        assert answer == 8484
