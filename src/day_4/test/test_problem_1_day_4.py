from src.day_4.problem_1 import Problem1Day4 as Problem


class TestProblem1Day4:
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

        assert answer == 13

    def test_aoc_answer(self):
        problem = Problem()
        answer = problem.answer()

        assert answer == 1467
