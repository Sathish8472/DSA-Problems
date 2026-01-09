# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def postOrder(node):
            if not node:
                return None, 0
            
            left_lca, left_depth = postOrder(node.left)
            right_lca, right_depth = postOrder(node.right)

            if not node.left and not node.right:
                return node, 1
            
            if left_depth == right_depth:
                return node, left_depth + 1
            elif left_depth > right_depth:
                return left_lca, left_depth + 1
            else:
                return right_lca, right_depth + 1


        lca, depth = postOrder(root)
        return lca
        