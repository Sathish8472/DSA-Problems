class Solution:

    # Binary Search implementationv - Lower bound
    # time: O(Log N)
    def searchInsert(self, nums: List[int], target: int) -> int:

        n = len(nums)
        left, right = 0, len(nums) - 1
        ans = n

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


    # Using Bisect
    def searchInsert1(self, nums: List[int], target: int) -> int:

        index = bisect.bisect_left(nums, target)
        print(index)

        return index
