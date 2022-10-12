from typing import List

"""
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.


Constraints:
    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        viewed = set()
        for value in nums:
            if value in viewed:
                return True

            viewed.add(value)

        return False


def test_base_case():
    assert_are_equal(Solution().containsDuplicate([1, 2, 3, 1]), True)


def test_many_duplicates():
    assert_are_equal(Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)


def test_no_duplicate():
    assert_are_equal(Solution().containsDuplicate([7, 6, 5, 4, 3, 1]), False)


def assert_are_equal(actual, expected):
    assert actual == expected, f"Expected: '{expected}' but got '{actual}'"


if __name__ == '__main__':
    test_base_case()
    test_many_duplicates()
    test_no_duplicate()
