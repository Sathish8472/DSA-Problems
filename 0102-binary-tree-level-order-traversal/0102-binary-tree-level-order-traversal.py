# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        result = []

        while queue:
            current_level = []

            for _ in range(len(queue)):
                node = queue.pop()

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

                current_level.append(node.val)
            result.append(current_level)

        return result
