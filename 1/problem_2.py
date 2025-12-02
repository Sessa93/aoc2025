import enum
from typing import List, Tuple

INITIAL_POSITION = 50
PASSWORD = 0
MAX_POSITION = 100

class RotationDirection(enum.Enum):
    L = 'L'
    R = 'R'

def read_rotations_from_file(file_path) -> List[Tuple[RotationDirection, int]]:
    with open(file_path, 'r') as file:
        return [(RotationDirection(line[0]), int(line[1:])) for line in file.readlines() if len(line) > 0]

def read_rotations_from_string(input_str: str) -> List[Tuple[RotationDirection, int]]:
    return [(RotationDirection(line.strip()[0]), int(line.strip()[1:])) for line in input_str.strip().split('\n') if len(line.strip()) > 0]

def update_position(start_position, degrees) -> Tuple[int, int]:
    full_rotations = abs(degrees) // MAX_POSITION
    abs_degrees = abs(degrees) % MAX_POSITION

    if degrees > 0:
        partial_rotations = 1 if abs_degrees >= (MAX_POSITION - start_position) else 0
    else:
        partial_rotations = 1 if abs_degrees >= start_position else 0

    if start_position == 0:
        partial_rotations = 0

    return full_rotations + partial_rotations, (start_position + degrees) % MAX_POSITION

def get_password(directions: List[Tuple[RotationDirection, int]]) -> int:
    position = INITIAL_POSITION
    password = 0
    for direction, degrees in directions:
        if direction == RotationDirection.L:
            degrees = -degrees
        passes, end_position = update_position(start_position=position, degrees=degrees)
        password += passes
        position = end_position
    return password

if __name__ == '__main__':
    test_1 = "R1000\n"
    res = get_password(directions=read_rotations_from_string(test_1))
    print('Password: ', res)
    assert res == 10

    test_2 = """
        L68
        L30
        R48
        L5
        R60
        L55
        L1
        L99
        R14
        L82
    """
    res = get_password(directions=read_rotations_from_string(test_2))
    print('Password: ', res)
    assert res == 6

    res = get_password(directions=read_rotations_from_file('./input_1.txt'))
    print('Password: ', res)
    assert res == 6475
