from typing import List


def check_if_repetition(id_to_test: str) -> bool:
    return True


def search_invalid(input_range: str) -> List[str]:
    output_list = []
    for id_to_test in input_range.split('-'):
        if check_if_repetition(id_to_test):
            output_list.append(int(id_to_test))
    return output_list
