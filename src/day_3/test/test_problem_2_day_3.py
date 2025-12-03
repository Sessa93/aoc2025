from src.day_3.problem_2 import Problem2


class TestProblem1Day3:
    def test_simple_case(self):
        input = """
            987654321111111
            811111111111119
            234234234234278
            818181911112111
        """

        problem = Problem2(input=input)
        answer = problem.answer()

        assert answer == 3121910778619

    def test_aoc_answer(self):
        problem = Problem2()
        answer = problem.answer()

        assert answer == 17196
