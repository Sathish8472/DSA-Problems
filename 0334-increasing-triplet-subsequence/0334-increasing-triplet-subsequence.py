class Solution:

    def increasingTriplet(self, nums: List[int]) -> bool:
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

        