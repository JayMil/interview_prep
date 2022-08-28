from typing import *

"""
55. Jump Game [Medium]

constraints
* Each element in array represents you maximum jump length
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        endPos = len(nums) - 1
        curPos = 0
        curOptions = 0
        badPositions = dict()
        optionsStack = [nums[curPos]]

        while curPos < endPos and len(optionsStack) > 0:
            jumpPos = optionsStack[len(optionsStack)-1]

            options = nums[curPos]
            curOptions = min(options, len(nums) - 1 - curPos)

        return True


        if options == 0:
            return False

        for jumps in range(options, 0, -1):
            if canJump(nums[jumps:]):
                return True

        return False

if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    assert canJump(nums)
    nums2 = [3, 2, 1, 0, 4]
    assert not canJump(nums2)
    nums3 = [1]
    assert canJump(nums3)
    nums3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1]
    assert not canJump(nums3)

    nums4 = [2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9, 6, 8, 8, 0, 6, 3, 1, 2, 2, 1, 2, 6, 5, 3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0, 0, 3, 8, 2, 4, 0, 1, 2, 0, 1, 4, 6, 5, 8, 0, 7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4, 3, 7, 0, 4, 9, 0, 9, 8, 4, 3, 0, 7, 7, 1, 9, 1, 9, 4, 9, 0, 1, 9, 5, 7, 7, 1, 5, 8, 2, 8, 2, 6, 8, 2, 2, 7, 5, 1, 7, 9, 6]
    assert not canJump(nums4)

