from typing import *

"""
238. Product of Array Except Self

Given an integer array nums, 
return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result: List[int] = list()

        # iterate over nums in reverse order to define products on left
        right_product = 1
        i = len(nums) - 1
        while i >= 0:
            right_product = right_product * nums[i]
            result.insert(0, right_product)
            i -= 1

        # iterate over nums and calculate right products and combine
        left_product = 1
        i = 0
        while i < len(nums):
            if i == 0:
                result[i] = result[i + 1]
            elif i == len(nums) - 1:
                result[i] = left_product
            else:
                result[i] = result[i + 1] * left_product

            left_product = left_product * nums[i]

            i += 1

        return result


def test_base_case():
    assert_are_equal(Solution().productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

def test_with_negative():
    assert_are_equal(Solution().productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])

def assert_are_equal(actual, expected):
    assert actual == expected, f"Expected: '{expected}' but got '{actual}'"


if __name__ == '__main__':
    test_base_case()
    test_with_negative()



