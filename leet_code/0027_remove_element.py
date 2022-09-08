from typing import *

"""
27. Remove Element

constraints
* remove occurrences in place
* must use O(1) extra memory
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            while left < right and nums[left] != val:
                left += 1

            while left < right and nums[right] == val:
                right -= 1

            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
                left += 1

        if left == right and nums[left] != val:
            left += 1

        return left


def test(nums: List[int], val: int, expected_length: int, expected_list: List[int]) -> None:
    k = Solution().removeElement(nums, val)

    assert k == expected_length, f"Length mismatch. Expected: {expected_length} but got {k}"
    for i in range(k):
        assert nums[i] == expected_list[i], f"Value mismatch. Expected: {expected_list[i]} but got {nums[i]}"


def test_base_case():
    test(nums=[3, 2, 2, 3], val=3, expected_length=2, expected_list=[2, 2])


def test_base_case2():
    test(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2, expected_length=5, expected_list=[0, 1, 4, 0, 3])


def test_no_match():
    test(nums=[2, 2, 2, 2], val=3, expected_length=4, expected_list=[2, 2, 2, 2])


def test_first_match_only():
    test(nums=[3, 2, 2, 2], val=3, expected_length=3, expected_list=[2, 2, 2])


def test_last_match_only():
    test(nums=[2, 2, 2, 3], val=3, expected_length=3, expected_list=[2, 2, 2])


def test_empty():
    test(nums=[], val=3, expected_length=0, expected_list=[])


def test_all_match():
    test(nums=[3, 3, 3], val=3, expected_length=0, expected_list=[])


def test_first_no_match():
    test(nums=[2, 3, 3, 3], val=3, expected_length=1, expected_list=[2])


def test_last_no_match():
    test(nums=[3, 3, 3, 2], val=3, expected_length=1, expected_list=[2])


if __name__ == '__main__':
    test_base_case()
    test_base_case2()
    test_no_match()
    test_first_match_only()
    test_last_match_only()
    test_empty()
    test_all_match()
    test_first_no_match()
    test_last_no_match()

