# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        to_delete_set = set(to_delete)
        forest = []

        def dfs(node, has_parent):
            if not node:
                return None
            
            root_deleted = node.val in to_delete_set
            if not root_deleted and not has_parent:
                forest.append(node)
            
            node.left = dfs(node.left, not root_deleted)
            node.right = dfs(node.right, not root_deleted)

            return None if root_deleted else node

        dfs(root, False)
        return forest
        