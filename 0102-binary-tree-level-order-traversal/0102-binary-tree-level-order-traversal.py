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

        queue = deque([root])
        result = []

        while queue:
            current_level = []

            for _ in range(len(queue)):
                node = queue.popleft()
                print("Current: ", node.val)

                current_level.append(node.val)
                if node.left:
                    print("left:", node.left.val)
                    queue.append(node.left)
                if node.right:
                    print("right:", node.right.val)
                    queue.append(node.right)
                

            print(current_level)
            result.append(current_level)

        return result
