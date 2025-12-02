import abc
from pathlib import Path
from typing import Any


class AbstractProblem(abc.ABC):
    def __init__(self, name: str, input: Any = Path(__file__).parent / "data/input.txt"):
        self.name = name
        if self.is_str_input(input_data=input):
            self.input = self.get_input_from_string(input_string=input)
        else:
            self.input = self.get_input_from_file(file_path=input)

    def __repr__(self):
        return f"Answer to problem {self.name}: {self.answer()}"

    @staticmethod
    def is_str_input(input_data: Any) -> bool:
        return isinstance(input_data, str)

    @staticmethod
    def is_file_input(input_data: Any) -> bool:
        return isinstance(input_data, Path)

    @abc.abstractmethod
    def get_input_from_file(self, file_path: str) -> str:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_input_from_string(self, input_string: str) -> str:
        raise NotImplementedError()

    @abc.abstractmethod
    def answer(self) -> Any:
        raise NotImplementedError()