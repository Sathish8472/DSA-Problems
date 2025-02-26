# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        postorder_index = len(postorder) - 1

        def construct(left: int, right: int) -> Optional[TreeNode]:
            nonlocal postorder_index

            if left > right:
                return None

            root_value = postorder[postorder_index]
            postorder_index -= 1
            root = TreeNode(root_value)

            inorder_index = inorder_index_map[root_value]

            root.right = construct(inorder_index + 1, right)
            root.left = construct(left, inorder_index - 1)

            return root

        return construct(0, len(postorder) - 1)
        