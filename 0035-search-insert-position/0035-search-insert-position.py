class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        index = bisect.bisect_left(nums, target)
        print(index)

        return index
        