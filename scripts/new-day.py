#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "rich",
#     "typer>=0.20.0",
# ]
# ///
from pathlib import Path
from typing import Annotated

import typer
from rich import print

app = typer.Typer()

BASE_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = BASE_DIR / Path("src")

PROBLEM_TEMPLATE = """
from typing import Any

from src.base.abstract_problem import AbstractProblem


class Problem{{problem_number}}Day{{day}}(AbstractProblem):
    def __init__(self, input=None):
        super().__init__(day={{day}}, problem={{problem_number}}, input=input)
    
    def parse_input(self, input_string: str):
        raise NotImplementedError()
    
    def answer(self) -> Any:
        raise NotImplementedError()
"""

TEST_TEMPLATE = """
from src.day_{{day}}.problem_{{problem_number}} import Problem{{problem_number}}Day{{day}} as Problem


class TestProblem{{problem_number}}Day{{day}}:
    def test_simple_case(self):
        input = ""

        problem = Problem(input=input)
        answer = problem.answer()

        assert answer == 42
    
    def test_aoc_answer(self):
        problem = Problem()
        answer = problem.answer()

        assert answer == 42
"""


def get_day_dir(day: str) -> Path:
    return SRC_DIR / Path(f"day_{day}")


def get_data_dir(day: str) -> Path:
    return get_day_dir(day=day) / Path("data")


def get_test_dir(day: str) -> Path:
    return get_day_dir(day=day) / Path("test")


def create_data_file(day: str) -> None:
    data_file_path = get_data_dir(day=day) / Path(f"input.txt")
    with open(data_file_path, "w"): pass
    with open(get_data_dir(day=day) / '.gitkeep', "w"): pass

def create_problem_file(day: str, problem_number: int) -> None:
    problem_file_path = get_day_dir(day=day) / Path(f"problem_{problem_number}.py")
    with open(problem_file_path, "w") as fp:
        fp.write(
            PROBLEM_TEMPLATE.replace("{{day}}", day).replace(
                "{{problem_number}}", str(problem_number)
            )
        )


def create_test_file(day: str, problem_number: int) -> None:
    test_file_path = get_test_dir(day=day) / Path(
        f"test_problem_{problem_number}_day_{day}.py"
    )
    with open(test_file_path, "w") as fp:
        fp.write(
            TEST_TEMPLATE.replace("{{day}}", day).replace(
                "{{problem_number}}", str(problem_number)
            )
        )


def create_day_folder(day: str) -> None:
    day_dir = get_day_dir(day=day)
    day_dir.mkdir(parents=True, exist_ok=False)

    with open(day_dir / "__init__.py", "w"):
        pass


def create_data_folder(day: str) -> None:
    get_data_dir(day=day).mkdir(parents=True, exist_ok=True)


def create_test_folder(day: str) -> None:
    get_test_dir(day=day).mkdir(parents=True, exist_ok=True)

    with open(get_test_dir(day=day) / "__init__.py", "w"):
        pass


@app.command()
def new_day(day: Annotated[str, typer.Argument()]):
    create_day_folder(day=day)
    create_data_folder(day=day)
    create_test_folder(day=day)

    create_data_file(day=day)
    create_problem_file(day=day, problem_number=1)
    create_problem_file(day=day, problem_number=2)
    create_test_file(day=day, problem_number=1)
    create_test_file(day=day, problem_number=2)

    print(
        f"[green]Successfully created new day folder structure for Day {day}![/green]"
    )


if __name__ == "__main__":
    app()
