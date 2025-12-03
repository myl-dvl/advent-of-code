from day2.day2 import search_invalid


class TestDay2:
    def test_invalid_id(self):
        # GIVEN
        input_range = '11-22'
        expected = [11, 22]
        # WHEN
        actual = search_invalid(input_range)
        # THEN
        assert actual == expected
