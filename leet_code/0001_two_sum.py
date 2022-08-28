from typing import *

"""
1. Two Sum [Easy]

constraints
* you can return the answer in any order
* each input will have exactly one solution
* you man not use the same element twice
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        viewed_numbers = dict()

        for i, number in enumerate(nums):
            if (target - number) in viewed_numbers:
                return [viewed_numbers[(target-number)], i]
            else:
                viewed_numbers[number] = i


def assert_are_equal(actual, expected):
    assert actual == expected, f"Expected: '{expected}' but got '{actual}'"


def test_first_two_indexes():
    assert_are_equal(Solution().twoSum([2, 7, 11, 15], 9), [0, 1])


def test_last_two_indexes():
    assert_are_equal(Solution().twoSum([3, 2, 4], 6), [1, 2])


def test_only_two_indexes():
    assert_are_equal(Solution().twoSum([3, 3], 6), [0, 1])


def test_non_adjacent_indexes():
    assert_are_equal(Solution().twoSum([1, 2, 3, 4, 100, 5, 6, 7, 8, 9, 10, 11, 12, 13], 113), [4, 13])


if __name__ == '__main__':
    test_first_two_indexes()
    test_last_two_indexes()
    test_only_two_indexes()
    test_non_adjacent_indexes()

