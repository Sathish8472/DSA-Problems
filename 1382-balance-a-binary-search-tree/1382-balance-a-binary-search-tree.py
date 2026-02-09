# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        
        def make_tree(arr):
            if not arr:
                return None
            
            n = len(arr)
            idx = n // 2
            root = arr[idx]
            left = make_tree(arr[:idx])
            right = make_tree(arr[idx + 1:])

            root.left = left
            root.right = right
            return root
        
        def traverse(root):
            if not root:
                return
            else:
                traverse(root.left)
                arr.append(root)
                traverse(root.right)
        
        traverse(root)
        return make_tree(arr)

