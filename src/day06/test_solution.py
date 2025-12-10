import pytest

from src.day06.solution import solution_1, solution_2
from src.read_file_to_lines import read_file_to_lines

solution_1_testdata = [
    ("sample.txt", 4277556),
    ("input.txt", 6635273135233),
]

@pytest.mark.parametrize("filename,expected", solution_1_testdata)
def test_solution_1_with_sample(filename, expected):
    assert solution_1(read_file_to_lines(filename)) == expected

solution_2_testdata = [
    ("sample.txt", 3263827),
    # ("input.txt", ???),
]

@pytest.mark.parametrize("filename,expected", solution_2_testdata)
def test_solution_2_with_sample(filename, expected):
    assert solution_2(read_file_to_lines(filename, with_strip=False)) == expected
