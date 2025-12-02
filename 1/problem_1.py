import enum

INITIAL_POSITION = 50
POSITION_AT_ZERO = 0
MAX_POSITION = 100

class RotationDirection(enum.Enum):
    L = 'L'
    R = 'R'

def read_rotations(file_path):
    with open(file_path, 'r') as file:
        for line in file.readlines():
            direction = RotationDirection(line[0])
            degrees = int(line[1:])
            yield direction, degrees



if __name__ == '__main__':
    position = INITIAL_POSITION
    for direction, degrees in read_rotations('./input_1.txt'):
        if direction == RotationDirection.L:
            position -= degrees
        elif direction == RotationDirection.R:
            position += degrees
        position %= MAX_POSITION

        if position == 0:
            POSITION_AT_ZERO += 1
    print(f"Password: {POSITION_AT_ZERO}")