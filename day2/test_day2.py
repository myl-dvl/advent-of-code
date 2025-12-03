import pytest

from day2.day2 import search_invalid, check_if_repetition, extract_sides


class TestDay2:
    def test_invalid_id(self):
        # GIVEN
        input_range = '11-22'
        expected = [11, 22]
        # WHEN
        actual = search_invalid(input_range)
        # THEN
        assert actual == expected

    @pytest.mark.parametrize('input_id, expected', [
        ('11', True),
        ('22', True),
        ('99', True),
    ])
    def test_check_if_repetition(self, input_id, expected):
        # GIVEN
        # WHEN
        actual = check_if_repetition(input_id)
        # THEN
        assert actual == expected

    def test_extract_sides(self):
        # GIVEN
        input_range = '11-22'
        expected = (11, 22)
        # WHEN
        actual = extract_sides(input_range)
        # THEN
        assert actual == expected
