from typing import *

"""
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.

In how many distinct ways can you climb to the top


Example 1:
Input: n = 3
Output: 3
Explanation: there are three ways to climb to the top
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints
1 <= n <= 45

"""


class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one + two
            two = one
            one = temp

        return one




def test_three_steps():
    assert_are_equal(Solution().climbStairs(3), 3)


def test_five_steps():
    assert_are_equal(Solution().climbStairs(5), 8)


def assert_are_equal(actual, expected):
    assert actual == expected, f"Expected: '{expected}' but got '{actual}'"


if __name__ == '__main__':
    test_three_steps()
    test_five_steps()
