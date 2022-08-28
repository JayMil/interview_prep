from typing import *

"""
1338. Reduce Array Size to The Half [Medium]
"""


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        half_length = len(arr) / 2
        number_counts = dict()
        for number in arr:
            if number in number_counts:
                number_counts[number] += 1
            else:
                number_counts[number] = 1

        counts = sorted(number_counts.values(), reverse=True)
        count_sum = 0
        for i, count in enumerate(counts):
            count_sum += count
            if count_sum >= half_length:
                return i+1

        return 0


def assert_are_equal(actual, expected):
    assert actual == expected, f"Expected: '{expected}' but got '{actual}'"


def test_one_groups():
    assert_are_equal(Solution().minSetSize([3, 3, 3, 3, 3, 5, 5, 2, 2, 7]), 1)


def test_two_groups():
    assert_are_equal(Solution().minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]), 2)


def test_two_groups_with_numbers_mixed():
    assert_are_equal(Solution().minSetSize([3, 2, 3, 7, 3, 5, 5, 2, 3, 5]), 2)


def test_all_numbers_same():
    assert_are_equal(Solution().minSetSize([7, 7, 7, 7, 7, 7]), 1)


def test_single_digit():
    assert_are_equal(Solution().minSetSize([7]), 1)


def test_empty_array():
    assert_are_equal(Solution().minSetSize([]), 0)


def test_all_uniq_numbers():
    assert_are_equal(Solution().minSetSize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5)


if __name__ == '__main__':
    test_one_groups()
    test_two_groups()
    test_two_groups_with_numbers_mixed()
    test_all_numbers_same()
    test_single_digit()
    test_empty_array()
    test_all_uniq_numbers()

