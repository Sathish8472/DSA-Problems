class Solution:

    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_right = [0] * n
        max_val = 0

        max_right[n - 1] = nums[n - 1]
        for k in range(n - 2, -1, -1):
            val = max(nums[k], max_right[k + 1])
            max_right[k] = val
        
        max_left = nums[0]
        for j in range(1, n - 1):
            val = (max_left - nums[j]) * max_right[j + 1]
            max_val = max(max_val, val)
            max_left = max(max_left, nums[j])

        print("max_left: ", max_left)
        print("max right: ", max_right)
        return max_val

    # Brute force
    def maximumTripletValue_1(self, nums: List[int]) -> int:

        n = len(nums)
        max_val = 0

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    max_val = max(max_val, (nums[i] - nums[j]) * nums[k])
        
        return max_val

        