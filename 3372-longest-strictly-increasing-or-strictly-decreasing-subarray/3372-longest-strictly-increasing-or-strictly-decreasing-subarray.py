class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_length = 1
        n = len(nums)
        
        for start in range(n):
            current_length = 1
            for pos in range(start + 1, n):
                if nums[pos] > nums[pos - 1]:
                    current_length += 1
                else:
                    break

            max_length = max(max_length, current_length)


        for start in range(n):
            current_length = 1
            for pos in range(start + 1, n):
                if nums[pos] < nums[pos - 1]:
                    current_length += 1
                else:
                    break

            max_length = max(max_length, current_length)

        return max_length

