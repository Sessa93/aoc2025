from src.day_3.problem_1 import Problem1


class TestProblem1Day3:
    def test_simple_case(self):
        input = """
            987654321111111
            811111111111119
            234234234234278
            818181911112111
        """

        problem = Problem1(input=input)
        answer = problem.answer()

        assert answer == 357

    def test_aoc_answer(self):
        problem = Problem1()
        answer = problem.answer()

        assert answer == 17196
