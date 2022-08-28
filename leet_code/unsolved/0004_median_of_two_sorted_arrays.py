from typing import *

"""
4. Median of Two Sorted Arrays

constraints
* overall run time complexity should be O(log (m+n))
* one of the arrays could have length of zero
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # if one of the lists doesn't have any values - just calculate median of other list
        if len(nums1) == 0:
            return self.findMedian(nums2)
        elif len(nums2) == 0:
            return self.findMedian(nums1)

        even_dataset = (len(nums1) + len(nums2)) % 2 == 0
        if even_dataset:
            target_index = ((len(nums1) + len(nums2)) / 2) - 1
        else:
            target_index = ((len(nums1) + len(nums2) - 1) / 2)

        print(target_index)
        index = 0
        n1 = 0
        n2 = 0

        while index < target_index:
            if nums1[n1] < nums2[n2]:
                n1 += 1
            elif nums1[n1] > nums2[n2]:
                n2 += 1
            else:
                if n1 < len(nums1) - 1:
                    n1 += 1
                else:
                    n2 += 1
            index += 1

        if even_dataset:
            if nums1[n1] < nums2[n2]:
                if n1+1 < len(nums1) and nums1[n1+1] < nums2[n2]:
                    return (nums1[n1] + nums1[n1+1]) / 2
                else:
                    return (nums1[n1] + nums2[n2]) / 2
            else:
                if n2+1 < len(nums2) and nums2[n2+1] < nums1[n1]:
                    return (nums2[n2] + nums2[n2+1]) / 2
                else:
                    return (nums2[n2] + nums1[n1]) / 2
        else:
            return min(nums1[n1], nums2[n2])

    def findMedian(self, nums: List[int]) -> float:
        if len(nums) % 2 == 0:
            a = int((len(nums) / 2) - 1)
            return (nums[a] + nums[a + 1]) / 2
        else:
            return nums[int((len(nums) - 1) / 2)]


def assert_are_equal(actual, expected):
    assert actual == expected, f"Expected: '{expected}' but got '{actual}'"


def test_odd():
    assert_are_equal(Solution().findMedianSortedArrays([1, 3], [2]), 2.0)


def test_even():
    assert_are_equal(Solution().findMedianSortedArrays([1, 3], [2, 4]), 2.5)


def test_odd_with_duplicates():
    assert_are_equal(Solution().findMedianSortedArrays([1, 1, 1, 2, 3], [1, 1, 1, 3, 4, 5, 6, 7]), 2)


def test_even_with_duplicates():
    assert_are_equal(Solution().findMedianSortedArrays([1, 1, 1, 2, 3, 4], [1, 1, 1, 3, 4, 5, 6, 7]), 2.5)


def test_single_digit_in_first():
    assert_are_equal(Solution().findMedianSortedArrays([1], []), 1)


def test_single_digit_in_second():
    assert_are_equal(Solution().findMedianSortedArrays([], [1]), 1)


def test_all_in_first():
    assert_are_equal(Solution().findMedianSortedArrays([1, 2, 3], []), 2)


def test_all_in_second():
    assert_are_equal(Solution().findMedianSortedArrays([], [1, 2, 3]), 2)


def test_consecutive_middles_in_first():
    assert_are_equal(Solution().findMedianSortedArrays([1, 2], [-1, 3]), 1.5)


def test_all_same_odd():
    assert_are_equal(Solution().findMedianSortedArrays([2, 2, 2], [2, 2, 2, 2]), 2)


def test_all_same_even():
    assert_are_equal(Solution().findMedianSortedArrays([2, 2, 2, 2], [2, 2, 2, 2]), 2)


def test_single_and_double():
    assert_are_equal(Solution().findMedianSortedArrays([1], [2, 3]), 2)



if __name__ == '__main__':
    # test_even()
    # test_odd()
    # test_odd_with_duplicates()
    # test_even_with_duplicates()
    # test_single_digit_in_first()
    # test_single_digit_in_second()
    # test_all_in_first()
    # test_all_in_second()
    # test_consecutive_middles_in_first()
    # test_all_same_odd()
    # test_all_same_even()
    test_single_and_double()
