from src.day_4.problem_2 import Problem2


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

        problem = Problem2(input=input)
        answer = problem.answer()

        assert answer == 43

    def test_aoc_answer(self):
        problem = Problem2()
        answer = problem.answer()

        assert answer == 8484
