class Solution:
    def longestSubarray1(self, nums: List[int]) -> int:

        max_len = 0
        max_and = 0
        n = len(nums)

        for i in range(n):
            current_and = nums[i]
            for j in range(i, n):
                current_and &= nums[j]
                if current_and > max_and:
                    max_and = current_and
                    max_len = j - i + 1
                elif current_and == max_and:
                    max_len = max(max_len, j - i + 1)
        
        return max_len
            

    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        longest = current = 0

        for num in nums:
            if num == max_val:
                current += 1
                longest = max(longest, current)
            else:
                current = 0

        return longest
