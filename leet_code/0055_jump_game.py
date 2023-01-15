import pytest
from typing import *

"""
55. Jump Game [Medium]

You are given an integer array nums. 
You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.


constraints
* 1 <= nums.length <= 10^4
* 0 <= nums[i] <= 105


Example1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # iterate over indexes backwards
        goal = len(nums) - 1
        for i in reversed(range(goal)):
            if nums[i] + i >= goal:
                goal = i

        return goal == 0


class TestSolution2:
    def test_five_true(self):
        assert Solution().canJump([2, 3, 1, 1, 4]) is True

    def test_five_false(self):
        assert Solution().canJump([3, 2, 1, 0, 4]) is False

    def test_two_true(self):
        assert Solution().canJump([1, 2]) is True


if __name__ == '__main__':
    pytest.main()
