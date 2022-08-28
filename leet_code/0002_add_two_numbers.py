from typing import *

"""
2.  Add Two Numbers [Easy]

constraints
* two non-empty linked lists
* digits in reverse order
* numbers do not contain leading zeros
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_node = None
        sum_node_head = None
        carry_over = 0
        while l1 and l2:
            if sum_node is None:
                sum = l1.val + l2.val
                carry_over = sum // 10
                sum_node = ListNode(sum % 10)
                sum_node_head = sum_node
            else:
                sum = l1.val + l2.val + carry_over
                carry_over = sum // 10
                sum_node.next = ListNode(sum % 10)
                sum_node = sum_node.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            sum = l1.val + carry_over
            carry_over = sum // 10
            sum_node.next = ListNode(sum % 10)
            sum_node = sum_node.next
            l1 = l1.next

        while l2:
            sum = l2.val + carry_over
            carry_over = sum // 10
            sum_node.next = ListNode(sum % 10)
            sum_node = sum_node.next
            l2 = l2.next

        if carry_over:
            sum_node.next = ListNode(carry_over)

        return sum_node_head


def TransformListToLinkedList(arr: list) -> ListNode:
    head = ListNode(arr[0])
    last = head
    for value in arr[1:]:
        last.next = ListNode(value)
        last = last.next

    return head


def TransformLinkedListToList(node: ListNode) -> List[int]:
    values = []
    while node.next:
        values.append(node.val)
        node = node.next
    values.append(node.val)
    return values


def test_add_three_digit_number():
    l1 = TransformListToLinkedList([2, 4, 3])
    l2 = TransformListToLinkedList([5, 6, 4])
    sl = TransformLinkedListToList(Solution().addTwoNumbers(l1, l2))
    assert_are_equal(sl, [7, 0, 8])


def test_add_zeros():
    l1 = TransformListToLinkedList([0])
    l2 = TransformListToLinkedList([0])
    sl = TransformLinkedListToList(Solution().addTwoNumbers(l1, l2))
    assert_are_equal(sl, [0])


def test_add_nines():
    l1 = TransformListToLinkedList([9, 9, 9, 9, 9, 9, 9])
    l2 = TransformListToLinkedList([9, 9, 9, 9])
    sl = TransformLinkedListToList(Solution().addTwoNumbers(l1, l2))
    assert_are_equal(sl, [8, 9, 9, 9, 0, 0, 0, 1])


def assert_are_equal(actual, expected):
    assert actual == expected, f"Expected: '{expected}' but got '{actual}'"


if __name__ == '__main__':
    test_add_three_digit_number()
    test_add_zeros()
    test_add_nines()
