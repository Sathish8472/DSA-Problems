# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtree_map = defaultdict(int)
        duplicates = []

        def serialize(node):
            if not node:
                return '#'
            
            left = serialize(node.left)
            right = serialize(node.right)
            subtree = f"{node.val},{left},{right}"

            subtree_map[subtree] += 1
            if subtree_map[subtree] == 2:
                duplicates.append(node)
            
            return subtree

        serialize(root)
        return duplicates
        