from typing import *

"""
167. Two Sum II [Medium]

constraints
* return the indices of the two numbers added by one
* each input will have exactly one solution
* you man not use the same element twice
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            sum = numbers[start] + numbers[end]
            if sum == target:
                return [start + 1, end + 1]
            elif sum > target:
                end -= 1
            else:
                start += 1


def assert_are_equal(actual, expected):
    assert actual == expected, f"Expected: '{expected}' but got '{actual}'"


def test_first_two_indexes():
    assert_are_equal(Solution().twoSum([2, 7, 11, 15], 9), [1, 2])


def test_first_and_last_indexes():
    assert_are_equal(Solution().twoSum([2, 3, 4], 6), [1, 3])


def test_only_two_with_negative():
    assert_are_equal(Solution().twoSum([-1, 0], -1), [1, 2])


if __name__ == '__main__':
    test_first_two_indexes()
    test_first_and_last_indexes()
    test_only_two_with_negative()
