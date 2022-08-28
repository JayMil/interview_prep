

"""
235. Lowest Common Ancestor of a Binary Search Tree [Easy]

* p and q are descendants of T
* a node can be a descendant of itself
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def add_node(self, x):
        if x < self.val:
            if self.left is None:
                self.left = TreeNode(x)
            else:
                self.left.add_node(x)
        else:
            if self.right is None:
                self.right = TreeNode(x)
            else:
                self.right.add_node(x)


def transform_list_to_binary_tree(nums: list):
    head = TreeNode(nums[0])
    for n in nums[1:]:
        head.add_node(n)

    return head


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


def assert_are_equal(actual, expected):
    assert actual == expected, f"Expected: '{expected}' but got '{actual}'"


def test_parent_is_a_child():
    tree = transform_list_to_binary_tree([6, 2, 8, 0, 4, 7, 9, 3, 5])
    res = Solution().lowestCommonAncestor(tree, TreeNode(2), TreeNode(4))
    assert_are_equal(res.val, 2)


def test_parent_is_root():
    tree = transform_list_to_binary_tree([6, 2, 8, 0, 4, 7, 9, 3, 5])
    res = Solution().lowestCommonAncestor(tree, TreeNode(2), TreeNode(8))
    assert_are_equal(res.val, 6)


if __name__ == '__main__':
    test_parent_is_a_child()
    test_parent_is_root()

