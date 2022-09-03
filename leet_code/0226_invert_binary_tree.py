from typing import *

"""
226. Invert Binary Tree
"""

class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right

    def add_node(self, node: "TreeNode"):
        if node.val < self.val:
            if self.left is None:
                self.left = node
            else:
                self.left.add_node(node)
        elif node.val > self.val:
            if self.right is None:
                self.right = node
            else:
                self.right.add_node(node)
        else:
            raise Exception(f"Adding duplicate value to Tree {node.val}")

    def add_node_reverse(self, node: "TreeNode"):
        if node.val < self.val:
            if self.right is None:
                self.right = node
            else:
                self.right.add_node_reverse(node)
        elif node.val > self.val:
            if self.left is None:
                self.left = node
            else:
                self.left.add_node_reverse(node)
        else:
            raise Exception(f"Adding duplicate value to Tree {node.val}")

    def __eq__(self, other: Optional["TreeNode"]):
        if other is None:
            return False

        if self.val != other.val:
            return False

        return self.left == other.left and self.right == other.right

    def values(self) -> List[int]:
        vals = []
        nodeQueue = [self]
        while nodeQueue:
            currentNode = nodeQueue.pop(0)
            vals.append(currentNode.val)
            if currentNode.left is not None:
                nodeQueue.append(currentNode.left)

            if currentNode.right is not None:
                nodeQueue.append(currentNode.right)

        return vals

    def __str__(self):
        return f"{self.values()}"


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        if root.left is not None:
            self.invertTree(root.left)

        if root.right is not None:
            self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        return root


def create_tree(nums: List[int]) -> TreeNode:
    if len(nums) == 0:
        return None

    root = TreeNode(nums[0])
    for num in nums[1:]:
        root.add_node(TreeNode(num))

    return root


def create_inverse_tree(nums: List[int]) -> TreeNode:
    if len(nums) == 0:
        return None

    root = TreeNode(nums[0])
    for num in nums[1:]:
        root.add_node_reverse(TreeNode(num))

    return root


def assert_equal_trees(actual: TreeNode, expected: TreeNode):
    assert actual == expected, f"Expected: '{expected}' but got '{actual}'"


def test_base_tree():
    tree1 = create_tree([4, 2, 7, 1, 3, 6, 9])
    tree1 = Solution().invertTree(tree1)
    tree2 = create_inverse_tree([4, 2, 7, 1, 3, 6, 9])
    assert_equal_trees(tree1, tree2)


def test_three_nodes():
    tree1 = create_tree([3, 1, 2])
    tree1 = Solution().invertTree(tree1)
    tree2 = create_inverse_tree([3, 1, 2])
    assert_equal_trees(tree1, tree2)


def test_empty_tree():
    tree1 = create_tree([])
    tree1 = Solution().invertTree(tree1)
    tree2 = create_inverse_tree([])
    assert_equal_trees(tree1, tree2)


if __name__ == '__main__':
    test_base_tree()
    test_three_nodes()
    test_empty_tree()

