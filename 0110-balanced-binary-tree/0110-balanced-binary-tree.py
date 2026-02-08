# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        if self.getHeight(root) == -1:
            return False
        
        return True
        
    def getHeight(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        lh = self.getHeight(node.left)
        rh = self.getHeight(node.right)

        if lh == -1 or rh == -1:
            return -1
        
        if abs(lh - rh) > 1:
            return -1
        
        return max(lh, rh) + 1