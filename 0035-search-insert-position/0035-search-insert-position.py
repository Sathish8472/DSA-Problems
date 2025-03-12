class Solution:

    # Binary Search implementation
    # time: O(Log N)
    def searchInsert(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left


    # Using Bisect
    def searchInsert1(self, nums: List[int], target: int) -> int:

        index = bisect.bisect_left(nums, target)
        print(index)

        return index
