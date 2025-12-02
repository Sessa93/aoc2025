def load_ranges_from_string(ranges_string):
    return [range(int(start), int(end) + 1) for start, end in (part.split('-') for part in ranges_string.split(','))]

def load_ranges_from_file(file_path):
    with open(file_path, 'r') as f:
        ranges_string = f.read().strip()
        return [range(int(start), int(end) + 1) for start, end in (part.split('-') for part in ranges_string.split(','))]

def is_valid_id(id: int) -> bool:
    input_id = str(id)
    if len(input_id) % 2 != 0:
        return True

    mid = len(input_id) // 2
    first_half = input_id[:mid]
    second_half = input_id[mid:]

    return not first_half == second_half

def sum_invalid_ids_in_ranges(ranges):
    total_sum = 0
    for r in ranges:
        for i in r:
            if not is_valid_id(i):
                total_sum += i
    return total_sum


if __name__ == '__main__':
    test_1 = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

    res = sum_invalid_ids_in_ranges(load_ranges_from_string(test_1))
    print(res)
    assert res == 1227775554

    res = sum_invalid_ids_in_ranges(load_ranges_from_file('./input.txt'))
    print(res)
    assert res == 64215794229
