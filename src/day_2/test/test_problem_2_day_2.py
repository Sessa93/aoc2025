from src.day_2.problem_2 import Problem2


class TestProblem1Day2:
    def test_simple_input(self):
        simple_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

        problem = Problem2(input=simple_input)

        answer = problem.answer()

        assert answer == 4174379265

    def test_aoc_answer(self):
        problem = Problem2()

        answer = problem.answer()

        assert answer == 85513235135
