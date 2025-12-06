import pytest

from src.day2.day2 import search_invalid, extract_sides, compute_input, detect_repetition, \
    split_chunks


class TestDay2:
    def test_invalid_id(self):
        # GIVEN
        input_range = '11-22'
        expected = [11, 22]
        # WHEN
        actual = search_invalid(input_range)
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

    def test_find_replication_inside_range(self):
        # GIVEN
        input_range = '95-115'
        expected = [99, 111]
        # WHEN
        actual = search_invalid(input_range)
        # THEN
        assert actual == expected

    def test_no_replication_inside_range(self):
        # GIVEN
        input_range = '1698522-1698528'
        expected = []
        # WHEN
        actual = search_invalid(input_range)
        # THEN
        assert actual == expected

    def test_sum_of_replication_ids(self):
        # GIVEN
        input_str = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
        1698522-1698528,446443-446449,38593856-38593862,565653-565659,
        824824821-824824827,2121212118-2121212124"""
        expected = 4174379265
        # WHEN
        actual = compute_input(input_str)
        # THEN
        assert actual == expected


# @pytest.mark.skip(reason='Not implemented yet')
class TestPart2:
    @pytest.mark.parametrize('input_str, expected', [
        ('11', True),
        ('22', True),
        ('99', True),
        ('111', True),
        ('1010', True),
        ('1188511885', True),
        ('222222', True),
        ('446446', True),
        ('38593859', True),
        ('385938591', False),
    ])
    def test_detect_repeating_pattern_of_size_one(self, input_str, expected):
        # GIVEN
        # WHEN
        actual = detect_repetition(input_str)
        # THEN
        assert actual == expected

    @pytest.mark.parametrize('input_str, chunk_size, expected', [
        ('111', 1, {'1'}),
        ('1010', 2, {'10'}),
        ('1188511885', 5, {'11885'}),
        ('565656', 2, {'56'}),
        ('824824', 3, {'824'}),
        ('2121', 2, {'21'}),
        ('2121', 1, {'1', '2'}),
        ('1188511885', 3, {'118', '851', '188', '5'}),
    ])
    def test_split_chunks(self, input_str, chunk_size, expected):
        # GIVEN
        # WHEN
        actual = split_chunks(input_str, chunk_size)
        # THEN
        assert actual == expected
