class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for x in nums:
            idx = -1
            for j in range(1, x):
                if (j | (j + 1)) == x:
                    idx = j
                    break
            
            ans.append(idx)
    
        return ans