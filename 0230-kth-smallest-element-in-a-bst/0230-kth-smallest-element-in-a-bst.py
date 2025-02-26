# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Recursive Inorder Traversal with Early Stop
    # Time: O(k), Space: O(H)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = None

        def inorder(node):
            nonlocal result, k
            if not node or result is not None:
                return
            
            inorder(node.left)
            
            k -= 1
            if k == 0:
                result = node.val
                return

            inorder(node.right)

        inorder(root)
        print(result)
        return result
