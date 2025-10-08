import sys
import os
import pytest

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_all_positive():
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_all_negative():
    assert longest_positive_streak([-1, -2, -3]) == 0

def test_all_zeros():
    assert longest_positive_streak([0, 0, 0]) == 0

def test_mixed_numbers_single_streak():
    assert longest_positive_streak([-1, 1, 2, 0, -3]) == 2

def test_multiple_streaks_longest_first():
    assert longest_positive_streak([1, 2, 3, -1, 4, 5, 0]) == 3

def test_multiple_streaks_longest_last():
    assert longest_positive_streak([1, 2, -1, 3, 4, 5, 0]) == 3

def test_streaks_with_zeros():
    assert longest_positive_streak([1, 0, 2, 3, 0, 4, 5, 6]) == 3

def test_streaks_with_negatives():
    assert longest_positive_streak([1, -2, 3, 4, -5, 6, 7, 8]) == 3

def test_no_positive_numbers():
    assert longest_positive_streak([-1, -5, 0, -10]) == 0

def test_single_element_positive():
    assert longest_positive_streak([5]) == 1

def test_single_element_negative():
    assert longest_positive_streak([-5]) == 0

def test_long_list():
    assert longest_positive_streak([1] * 100) == 100
    assert longest_positive_streak(([1, 2, -1] * 50) + [3] * 101) == 101