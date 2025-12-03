import importlib
import inspect
import pkgutil
from typing import Optional

from typing_extensions import Annotated

import typer

from src.base.abstract_problem import AbstractProblem
from rich import print

app = typer.Typer()

def iter_problem_classes(package_name: str):
    package = importlib.import_module(package_name)
    seen = set()

    for finder, name, is_pkg in pkgutil.walk_packages(
        package.__path__, package.__name__ + "."
    ):
        try:
            module = importlib.import_module(name)
        except Exception:
            continue

        for _, obj in inspect.getmembers(module, inspect.isclass):
            if (
                issubclass(obj, AbstractProblem)
                and obj is not AbstractProblem
                and obj.__module__.startswith(package_name)
            ):
                key = (obj.__module__, obj.__name__)
                if key in seen:
                    continue
                seen.add(key)
                yield obj


def run(package_name: str = "src", day: int = None, problem: int = None):
    for cls in iter_problem_classes(package_name):
        try:
            if day and problem:
                if f"day_{day}.problem_{problem}" in str(cls):
                    print(cls())
                    break
            else:
                print(cls())
        except Exception as exc:
            print(f"Error running {cls.__module__}.{cls.__name__}: {exc}")

@app.command()
def run_all():
    """Run all problems in the src package."""
    run()

@app.command()
def run_single(
        day: int = Annotated[Optional[int], typer.Option( min=1, max=12)],
        problem: int = Annotated[Optional[int], typer.Option("-p", min=1, max=2)],
):
    run(day=day, problem=problem)

if __name__ == "__main__":
    app()