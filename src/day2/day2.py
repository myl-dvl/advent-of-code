from pathlib import Path
from typing import List, Tuple

from src.utils import import_text


def search_invalid(input_range: str) -> List[int]:
    output_list = []
    start, end = extract_sides(input_range)
    for id_to_test in range(start, end + 1):
        if detect_repetition(str(id_to_test)):
            output_list.append(id_to_test)
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


def detect_repetition(input_str):
    if len(input_str) <= 1:
        return False
    else:
        for chunk_size in range(1, len(input_str) // 2 + 1):
            chunk_set = split_chunks(input_str, chunk_size)
            if len(chunk_set) == 1:
                return True
        else:
            return False


def split_chunks(input_str: str, chunk_size: int) -> set[str]:
    return {input_str[i:i + chunk_size] for i in range(0, len(input_str), chunk_size)}


if __name__ == '__main__':
    puzzle_str = import_text(Path('../../input/day2.txt'))
    print(f'Sum replication ids: {compute_input(puzzle_str[0])}')
