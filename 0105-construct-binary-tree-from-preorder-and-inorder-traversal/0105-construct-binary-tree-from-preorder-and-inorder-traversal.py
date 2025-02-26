# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        preorder_index = 0

        def construct(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preorder_index
            if left > right:
                return None
            
            root_value = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(root_value)

            inorder_index = inorder_index_map[root_value]

            root.left = construct(left, inorder_index - 1)
            root.right = construct(inorder_index + 1, right)

            return root

        return construct(0, len(inorder) - 1)




        