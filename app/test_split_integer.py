import pytest

from app.split_integer import split_integer


def test_should_split_into_one_part_when_number_of_parts_is_one():
    assert split_integer(8, 1) == [8]


def test_should_return_parts_equal_to_value_when_value_equals_number_of_parts():
    assert split_integer(1, 1) == [1]
    assert split_integer(5, 5) == [1, 1, 1, 1, 1]


def test_should_return_parts_with_zeros_when_value_is_less_than_number_of_parts():
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]


def test_should_split_into_equal_parts_when_value_divisible_by_number_of_parts():
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(12, 4) == [3, 3, 3, 3]


def test_should_return_sorted_parts_when_value_not_divisible_by_number_of_parts():
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


@pytest.mark.parametrize(
    "value, number_of_parts",
    [(8, 1), (6, 2), (17, 4), (32, 6), (3, 5), (100, 7)],
)
def test_should_return_exactly_number_of_parts_elements(value, number_of_parts):
    assert len(split_integer(value, number_of_parts)) == number_of_parts


@pytest.mark.parametrize(
    "value, number_of_parts",
    [(8, 1), (6, 2), (17, 4), (32, 6), (3, 5), (100, 7)],
)
def test_should_return_parts_with_difference_not_more_than_one(value, number_of_parts):
    parts = split_integer(value, number_of_parts)
    assert max(parts) - min(parts) <= 1


@pytest.mark.parametrize(
    "value, number_of_parts",
    [(8, 1), (6, 2), (17, 4), (32, 6), (3, 5), (100, 7)],
)
def test_should_return_parts_sorted_ascending(value, number_of_parts):
    parts = split_integer(value, number_of_parts)
    assert parts == sorted(parts)


@pytest.mark.parametrize(
    "value, number_of_parts",
    [(8, 1), (6, 2), (17, 4), (32, 6), (3, 5), (100, 7)],
)
def test_should_return_parts_with_sum_equal_to_value(value, number_of_parts):
    assert sum(split_integer(value, number_of_parts)) == value
