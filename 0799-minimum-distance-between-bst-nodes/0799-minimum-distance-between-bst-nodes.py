# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        if not root:
            return None

        min_diff = float('inf')
        prev = None

        def inorder(node):
            nonlocal min_diff, prev
            if not node:
                return None

            inorder(node.left)
            if prev is not None:
                min_diff = min(min_diff, node.val - prev)
            prev = node.val
            inorder(node.right)

        inorder(root)
        return min_diff;
        