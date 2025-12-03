import importlib
import inspect
import os
import pkgutil

from src.base.abstract_problem import AbstractProblem


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


def run_all_problems(package_name: str = "src"):
    for cls in iter_problem_classes(package_name):
        day = os.environ.get('DAY')
        problem = os.environ.get('PROBLEM')
        try:
            if day and problem:
                if f"day_{day}.problem_{problem}" in str(cls):
                    print(cls())
                    break
            else:
                print(cls())
        except Exception as exc:
            print(f"Error running {cls.__module__}.{cls.__name__}: {exc}")


if __name__ == "__main__":
    run_all_problems()
