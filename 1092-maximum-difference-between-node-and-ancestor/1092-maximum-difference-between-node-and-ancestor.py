# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = 0
        def helper(node, cur_max, cur_min):
            nonlocal result
            if not node:
                return
            print("node val: ", node.val)
           
            result = max(result, abs(cur_max - node.val), abs(cur_min - node.val))
            print("Max:", cur_max, ", Min: ", cur_min)
            
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            helper(node.left, cur_max, cur_min)
            helper(node.right, cur_max, cur_min)

        helper(root, root.val, root.val)
        return result

        