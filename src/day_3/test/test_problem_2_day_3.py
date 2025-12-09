from src.day_3.problem_2 import Problem2Day3 as Problem


class TestProblem1Day3:
    def test_simple_case(self):
        input = """
            987654321111111
            811111111111119
            234234234234278
            818181911112111
        """

        problem = Problem(input=input)
        answer = problem.answer()

        assert answer == 3121910778619

    def test_aoc_answer(self):
        problem = Problem()
        answer = problem.answer()

        assert answer == 171039099596062
