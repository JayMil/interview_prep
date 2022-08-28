from typing import *

"""
15. 3Sum [Medium]

constraints
* Solution set must not contain duplicate triplets
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        start = 0
        middle = 1
        end = len(nums) - 1
        results = []

        while middle < end:
            while middle < end:
                sum = nums[start] + nums[middle] + nums[end]
                if sum == 0:
                    indexes = [nums[start], nums[middle], nums[end]]
                    if indexes not in results:
                        results.append(indexes)
                    end -= 1
                elif sum < 0:
                    middle += 1
                else:
                    end -= 1

            start += 1
            middle = start + 1
            end = len(nums) - 1

        return results


def assert_are_equal(actual, expected):
    assert actual == expected, f"Expected: '{expected}' but got '{actual}'"


def test_two_sets():
    assert_are_equal(Solution().threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])


def test_no_match():
    assert_are_equal(Solution().threeSum([0, 1, 1]), [])


def test_all_zeros():
    assert_are_equal(Solution().threeSum([0, 0, 0]), [[0, 0, 0]])


if __name__ == '__main__':
    test_two_sets()
    test_no_match()
    test_all_zeros()
