from pathlib import Path

from src.utils import extract_text, import_text


def test_extract_text():
    # GIVEN
    input_text = """
                L68
                L30
                R48
                L5
                R60
                L55
                L1
                L99
                R14
                L82
                """
    expected = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
    # WHEN
    actual = extract_text(input_text)
    # THEN
    assert actual == expected

def test_import_text():
    # GIVEN
    input_path = Path('tests/test.txt')
    expected = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
    # WHEN
    actual = import_text(input_path)
    # THEN
    assert actual == expected
