from pathlib import Path
from typing import List, Tuple

from src.utils import import_text


class Dial:
    def __init__(self, starting_pos: int):
        self.current_pos = starting_pos
        self.size = 100

    @property
    def pos(self):
        return self.current_pos

    def rotate(self, input_command: str) -> int:
        direction, distance = self._extract_command(input_command)
        extra_rotations = self._count_extra_rotations(distance)
        distance = distance - extra_rotations * self.size
        new_pos = None
        match direction:
            case 'R':
                new_pos = self.current_pos + distance
            case 'L':
                new_pos = self.current_pos - distance
            case _:
                raise ValueError('Invalid direction')
        if new_pos <= 0 or new_pos >= self.size:
            if self.current_pos != 0:
                extra_rotations += 1
            new_pos = self._correct_pos(new_pos)
        self.current_pos = new_pos
        return extra_rotations

    def full_process(self, input_command: List[str]) -> int:
        final_score = 0
        for command in input_command:
            if self.rotate(command):
                final_score += 1
        return final_score

    @staticmethod
    def _extract_command(input_command) -> Tuple[str, int]:
        return input_command[0], int(input_command[1:])

    @staticmethod
    def _check_if_at_0_pos(current_pos: int) -> bool:
        return current_pos == 0

    @staticmethod
    def _count_extra_rotations(distance: int) -> int:
        distance_str = str(distance)
        if len(distance_str) <= 2:
            return 0
        n_extra_rotations_str = distance_str[:-2]
        return int(n_extra_rotations_str)

    def _correct_pos(self, new_pos: int) -> int:
        if new_pos < 0:
            return self.size + new_pos
        elif new_pos >= self.size:
            return new_pos - self.size
        else:
            return new_pos


if __name__ == '__main__':
    # test_list = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
    list_input = import_text(Path('../../input/day1.txt'))
    dial = Dial(50)
    print(f'final_score: {dial.full_process(list_input)}')
