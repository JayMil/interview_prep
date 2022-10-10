from typing import *

"""
42. Trapping Rain Water
"""

class Solution:
    def trap(self, heights: List[int]) -> int:
        return self.trap_n(heights)

    def trap_n(self, heights: List[int]) -> int:
        if len(heights) < 3:
            return 0

        left, right = 0, len(heights) - 1
        max_left, max_right = heights[left], heights[right]
        holding = 0

        while left + 1 != right:
            print(heights[left], heights[right], max_left, max_right, holding)
            if max_left <= max_right:
                left += 1
                if heights[left] < max_left:
                    holding += max_left - heights[left]
                elif heights[left] > max_left:
                    max_left = heights[left]
            else:
                right -= 1
                if heights[right] < max_right:
                    holding += max_right - heights[right]
                elif heights[right] > max_right:
                    max_right = heights[right]

        return holding



    def trap_n_squared(self, heights: List[int]) -> int:
        holding = 0

        # iterate over all but first and last value as they will never hold
        for i in range(1, len(heights)-1):
            height = heights[i]
            l = i - 1
            r = i + 1
            l_max = 0
            r_max = 0


            while l > 0 or r < len(heights):
                l_wall = heights[l]
                r_wall = heights[r]
                l_max = max(l_wall, l_max)
                r_max = max(r_wall, r_max)

                if l == 0 and r == len(heights) - 1:
                    break

                if l > 0:
                    l -= 1

                if r < len(heights)-1:
                    r += 1

            pen_wall = min(l_max, r_max)

            if pen_wall > height:
                holding += pen_wall - height

        return holding


def assert_are_equal(actual, expected):
    assert actual == expected, f"Expected: '{expected}' but got '{actual}'"


def test_base_case():
    assert_are_equal(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)


def test_base_case2():
    assert_are_equal(Solution().trap([4, 2, 0, 3, 2, 5]), 9)

if __name__ == '__main__':
    test_base_case()
    test_base_case2()
