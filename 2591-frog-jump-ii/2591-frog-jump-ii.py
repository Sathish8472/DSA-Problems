class Solution:
    def maxJump(self, stones: List[int]) -> int:

        max_jump = stones[1] - stones[0]

        for i in range(2, len(stones)):
            max_jump = max(max_jump, stones[i] - stones[i - 2])
        
        return max_jump
        