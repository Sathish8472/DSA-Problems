class Solution:

    # Greedy Optimal 
    def increasingTriplet_12(self, nums: List[int]) -> bool:
        first_num = second_num = float('inf')
        n = len(nums)

        for num in nums:
            if num <= first_num:
                first_num = num
            elif num <= second_num:
                second_num = num
            else:
                return True

        return False



    # Using Two Arrays Better approach
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        left_min = [float('inf')] * n
        right_max = [float('-inf')] * n

        left_min[0] = nums[0]
        for i in range(1, n):
            left_min[i] = min(left_min[i - 1], nums[i])

        right_max[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i])

        for i in range(1, n - 1):
            if left_min[i] < nums[i] < right_max[i]:
                return True

        return False



    # Brute force
    # time: O(N ^ 3)
    def increasingTriplet_1(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    if nums[i] < nums[j] < nums[k]:
                        return True

        return False

        