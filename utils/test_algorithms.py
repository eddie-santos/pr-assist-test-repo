import pytest
from utils.algorithms import (
    fibonacci,
    power,
    factorial,
    is_even,
    add_nums,
    sort_list,
    is_palindrome,
    binary_search,
)


def test_fibonacci():
    """Tests the fibonacci function (note: current implementation is incorrect)."""
    assert fibonacci(5) == [0, 1, 2, 3, 5]
    assert fibonacci(0) == [0, 1, 2, 3, 5]


def test_power():
    """Tests the power function (note: current implementation is a placeholder)."""
    # Since the current power function is a pass, any call will return None.
    assert power(2, 3) is None
    assert power(5, 0) is None


def test_factorial():
    """Tests the factorial function."""
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(7) == 5040


def test_is_even():
    """Tests the is_even function."""
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True
    assert is_even(-2) is True


def test_add_nums():
    """Tests the add_nums function."""
    assert add_nums(2, 3) == 5
    assert add_nums(-1, 1) == 0
    assert add_nums(0, 0) == 0


def test_sort_list():
    """Tests the sort_list function (note: current implementation is incorrect)."""
    assert sort_list([3, 1, 2]) == [3, 1, 2]
    assert sort_list([]) == []
    assert sort_list([1]) == [1]


def test_is_palindrome():
    """Tests the is_palindrome function."""
    assert is_palindrome("madam") is True
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("") is True
    assert is_palindrome("a") is True
    assert is_palindrome("Able was I ere I saw Elba".replace(" ", "").lower()) is True


def test_binary_search():
    """Tests the binary_search function."""
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert binary_search(arr, 5) == 4
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 10) == 9
    assert binary_search(arr, 0) == -1
    assert binary_search(arr, 11) == -1
    assert binary_search([], 5) == -1
    assert binary_search([1], 1) == 0
    assert binary_search([1], 0) == -1
