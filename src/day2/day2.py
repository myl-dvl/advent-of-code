from pathlib import Path
from typing import List, Tuple

from src.utils import import_text


def check_if_repetition(id_to_test: int) -> bool:
    str_id = str(id_to_test)
    if len(str_id) % 2 > 0:
        return False
    else:
        middle = len(str_id) // 2
        if str_id[:middle] == str_id[middle:]:
            return True
        else:
            return False


def search_invalid(input_range: str) -> List[int]:
    output_list = []
    start, end = extract_sides(input_range)
    for id_to_test in range(start, end + 1):
        if check_if_repetition(id_to_test):
            output_list.append(int(id_to_test))
    return output_list


def extract_sides(input_range: str) -> Tuple[int, int]:
    start, end = input_range.split('-')
    return int(start), int(end)


def compute_input(input_str: str) -> int:
    count = 0
    for range_str in input_str.split(','):
        list_invalid = search_invalid(range_str)
        count += sum(list_invalid)
    return count


if __name__ == '__main__':
    input_str = import_text(Path('day2.txt'))
    print(f'Sum replication ids: {compute_input(input_str[0])}')
    # 22062284697
