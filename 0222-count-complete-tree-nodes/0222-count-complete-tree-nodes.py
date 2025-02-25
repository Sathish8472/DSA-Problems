# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Binary Search + Recursion
    # Time: O(log^2 N), Space: O(log N)
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def getHeight(node):
            height = 0

            while node:
                height += 1
                node = node.left

            return height

        left_height = getHeight(root.left)
        right_height = getHeight(root.right)

        if left_height == right_height:
            # right subtree is perfect: count nodes directly
            return (1 << left_height) + self.countNodes(root.right)
        else:
            # right subtree is perfect: count nodes directly
            return (1 << right_height) + self.countNodes(root.left)

    def countNodes_2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [root]
        count = 0

        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

            count += 1

        return count

    # Linear time
    # Time: O(N), Space: O(log N)
    def countNodes_1(self, root: Optional[TreeNode]) -> int:
        return (
            1 + self.countNodes(root.right) + self.countNodes(root.left) if root else 0
        )
