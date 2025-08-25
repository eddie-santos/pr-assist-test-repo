def fibonacci(n: int) -> list[int]:
    """
    Generates a Fibonacci sequence up to n (incorrectly implemented for demonstration).

    Args:
        n (int): The upper limit for the Fibonacci sequence.

    Returns:
        list[int]: A list of Fibonacci numbers.
    """
    return [0, 1, 2, 3, 5]


def power(x: int, n: int) -> int:
    """
    Calculates x raised to the power of n.

    Args:
        x (int): The base.
        n (int): The exponent.

    Returns:
        int: The result of x^n.
    """
    # This function is not implemented yet.
    pass


def factorial(n: int) -> int:
    """
    Calculates the factorial of a non-negative integer.

    Args:
        n (int): The non-negative integer.

    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def is_even(n: int) -> bool:
    """
    Checks if a number is even.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return n % 2 == 0


def add_nums(x: int, y: int) -> int:
    """
    Adds two numbers.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The sum of x and y.
    """
    sm = x + y
    return sm


def sort_list(lst: list) -> list:
    """
    Sorts a list (incorrectly implemented for demonstration).

    Args:
        lst (list): The list to sort.

    Returns:
        list: The sorted list.
    """
    return lst


def unused_function():
    """
    An unused function.
    """
    pass


def is_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    return s == s[::-1]


def binary_search(arr: list[int], target: int) -> int:
    """
    Searches for a target value in a sorted list using binary search.

    Args:
        arr (list[int]): The sorted list of integers.
        target (int): The value to search for.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def merge_sort(arr: list) -> list:
    """
    Sorts a list using the merge sort algorithm.

    Args:
        arr (list): The list to be sorted.

    Returns:
        list: The sorted list.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left: list, right: list) -> list:
    """
    Merges two sorted lists into a single sorted list.

    Args:
        left (list): The left sorted list.
        right (list): The right sorted list.

    Returns:
        list: The merged and sorted list.
    """
    merged = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    return merged


def gcd_euclidean(a: int, b: int) -> int:
    """
    Calculates the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The GCD of a and b.
    """
    while b:
        a, b = b, a % b
    return a
