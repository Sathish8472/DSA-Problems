# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)

            # Push right first so left is processed first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result


    
    # Recursive Solution (Simple but Not Optimal)
    # Time: O(n) (since we visit each node once)
    # Space: O(n) (because of recursion stack)
    def preorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)