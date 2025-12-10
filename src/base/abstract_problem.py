import abc
import os
import time
from pathlib import Path
from typing import Any
from rich import print
from dotenv import load_dotenv
import requests


class AbstractProblem(abc.ABC):
    def __init__(self, day: int, problem_number: int, input: str = None):
        load_dotenv()

        self.name = f"Problem {problem_number} Day {day}"
        self.day = day
        self.problem_number = problem_number
        self.session_id = os.getenv("AOC_SESSION_ID")

        if input:
            self.input = self.parse_input(input)
        else:
            self.input = self.get_input()

    def __repr__(self):
        start = time.perf_counter()
        answer = self.answer()
        elapsed = time.perf_counter() - start

        return f"Answer to {self.name}: {answer}, execution time: {float(f'{elapsed:.4f}')} seconds"

    def get_input(self):
        input_file_path = (
            Path(__file__).parent.parent / f"day_{self.day}/data" / "input.txt"
        )
        try:
            with open(input_file_path, "r") as f:
                file_input = f.read().strip()
                return self.parse_input(input_string=file_input)
        except FileNotFoundError:
            print(f"{input_file_path} not found!")
            print(f"Fetching it from AoC...")
            remote_input = self.get_input_from_aoc()

            with open(input_file_path, "w") as f:
                f.write(remote_input)
            return self.parse_input(input_string=remote_input)

    @staticmethod
    def is_str_input(input_data: Any) -> bool:
        return isinstance(input_data, str)

    @staticmethod
    def is_file_input(input_data: Any) -> bool:
        return isinstance(input_data, Path)

    def get_input_from_aoc(self) -> str:
        remote_input = f"https://adventofcode.com/2025/day/{self.day}/input"
        return requests.get(remote_input, cookies={"session": self.session_id}).text

    @abc.abstractmethod
    def parse_input(self, input_string: str) -> str:
        raise NotImplementedError()

    @abc.abstractmethod
    def answer(self) -> Any:
        raise NotImplementedError()
