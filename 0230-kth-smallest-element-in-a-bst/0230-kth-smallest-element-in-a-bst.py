# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        result = []

        def dfs(node):
            if not node:
                return
            
            if node.left:
                dfs(node.left)
            
            result.append(node.val)

            if node.right:
                dfs(node.right)

        dfs(root)
        print(result)
        return result[k - 1]
