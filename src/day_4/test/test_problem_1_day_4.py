from src.day_4.problem_1 import Problem1


class TestProblem1Day3:
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

        problem = Problem1(input=input)
        answer = problem.answer()

        assert answer == 13

    def test_aoc_answer(self):
        problem = Problem1()
        answer = problem.answer()

        assert answer == 1467
