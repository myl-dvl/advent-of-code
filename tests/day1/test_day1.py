import pytest

from src.day1.day1 import Dial


@pytest.fixture
def dial():
    return Dial(50)


class TestDay1:
    def test_move_right(self):
        # GIVEN
        current_pos = 11
        dial = Dial(current_pos)
        input_command = 'R8'
        expected = 19
        # WHEN
        dial.rotate(input_command)
        # THEN
        actual = dial.pos
        assert actual == expected

    def test_move_left(self):
        # GIVEN
        current_pos = 19
        dial = Dial(current_pos)
        input_command = 'L19'
        expected = 0
        # WHEN
        dial.rotate(input_command)
        # THEN
        actual = dial.pos
        assert actual == expected

    def test_0_to_99(self):
        # GIVEN
        current_pos = 0
        dial = Dial(current_pos)
        input_command = 'L1'
        expected = 99
        # WHEN
        dial.rotate(input_command)
        # THEN
        actual = dial.pos
        assert actual == expected

    def test_99_to_0(self):
        # GIVEN
        current_pos = 99
        dial = Dial(current_pos)
        input_command = 'R1'
        expected = 0
        dial.rotate(input_command)
        # THEN
        actual = dial.pos
        assert actual == expected

    def test_move_backward(self):
        # GIVEN
        current_pos = 5
        dial = Dial(current_pos)
        input_command = 'L10'
        expected = 95
        # WHEN
        dial.rotate(input_command)
        # THEN
        actual = dial.pos
        assert actual == expected

    def test_move_full_turn(self):
        # GIVEN
        current_pos = 95
        dial = Dial(current_pos)
        input_command = 'R5'
        expected = 0
        # WHEN
        dial.rotate(input_command)
        # THEN
        actual = dial.pos
        assert actual == expected

    def test_count_when_zero(self, dial):
        # GIVEN
        list_input = ['R50', 'L5', 'R10']
        expected = 1
        # WHEN
        actual = dial.full_process(list_input)
        # THEN
        assert actual == expected

    def test_validation(self, dial):
        # GIVEN
        list_input = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
        expected = 3
        # WHEN
        actual = dial.full_process(list_input)
        # THEN
        assert actual == expected
