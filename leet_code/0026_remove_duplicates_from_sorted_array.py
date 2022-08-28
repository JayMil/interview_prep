from typing import *

"""
26. Remove Duplicates from Sorted Array [Easy]

constraints
* nums is sorted
* do not allocate extra space for another array.
* modify the existing array inplace with O(1) extra memory
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        swap_index = 1
        previous = None

        while i < len(nums):
            if previous is None:
                previous = nums[i]
            elif previous != nums[i]:
                previous = nums[i]

                # swap
                temp = nums[swap_index]
                nums[swap_index] = nums[i]
                nums[i] = temp

                swap_index += 1

            i += 1

        return swap_index


def test(nums: List[int], expected_length: int, expected_list: List[int]) -> None:
    k = Solution().removeDuplicates(nums)

    assert k == expected_length, f"Length mismatch. Expected: {expected_length} but got {k}"
    for i in range(k):
        assert nums[i] == expected_list[i], f"Value mismatch. Expected: {expected_list[i]} but got {nums[i]}"


def test_remove_single_duplicate():
    test(nums=[1, 1, 2], expected_length=2, expected_list=[1, 2])


def test_remove_multiple_duplicates():
    test(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4], expected_length=5, expected_list=[0, 1, 2, 3, 4])


def test_no_duplicates():
    test(nums=[0, 1, 2, 3, 4], expected_length=5, expected_list=[0, 1, 2, 3, 4])


def test_single_element():
    test(nums=[0], expected_length=1, expected_list=[0])

if __name__ == '__main__':
    test_remove_single_duplicate()
    test_remove_multiple_duplicates()
    test_no_duplicates()
    test_single_element()
