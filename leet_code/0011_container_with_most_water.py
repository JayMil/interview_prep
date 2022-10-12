from typing import *

"""
11. Container with most water

constraints
* heights will have a minimum length of 2
* An individual height will hava minimum of 0

"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            k = min(height[left], height[right])
            area = k * (right - left)
            maxArea = max(area, maxArea)

            if height[left] < height[right]:
                prev = height[left]
                left += 1
                while height[left] <= prev and left < right:
                    left += 1
            else:
                prev = height[right]
                right -= 1
                while height[right] <= prev and right > left:
                    right -= 1

        return maxArea


def assert_are_equal(actual, expected):
    assert actual == expected, f"Expected: '{expected}' but got '{actual}'"


def test_base_case():
    assert_are_equal(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)


def test_min_size():
    assert_are_equal(Solution().maxArea([1, 1]), 1)


def test_all_zeros():
    assert_are_equal(Solution().maxArea([0, 0, 0, 0, 0]), 0)


def test_ordered():
    assert_are_equal(Solution().maxArea([1, 2, 4, 3]), 4)

if __name__ == '__main__':
    test_base_case()
    test_all_zeros()
    test_min_size()
    test_ordered()
