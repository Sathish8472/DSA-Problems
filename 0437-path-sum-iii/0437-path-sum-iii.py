# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Using Prefix Sum (O(n))
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefixSum = defaultdict(int)
        prefixSum[0] = 1

        def dfs(node, currentSum):
            if not node:
                return 0

            currentSum += node.val
            count = prefixSum[currentSum - targetSum]
            prefixSum[currentSum] += 1

            count += dfs(node.left, currentSum) + dfs(node.right, currentSum)

            prefixSum[currentSum] -= 1
            return count
            
        return dfs(root, 0)

    # Brute Force
    # Time: O(N ^ 2)
    def pathSum_1(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        def countPathsFromNode(node, currentSum):
            if not node:
                return 0

            currentSum += node.val
            count = 1 if currentSum == targetSum else 0

            return (
                count
                + countPathsFromNode(node.left, currentSum)
                + countPathsFromNode(node.right, currentSum)
            )

        return (
            countPathsFromNode(root, 0)
            + self.pathSum(root.left, targetSum)
            + self.pathSum(root.right, targetSum)
        )
