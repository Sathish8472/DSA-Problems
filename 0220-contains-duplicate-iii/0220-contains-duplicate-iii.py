class Solution:

    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int):

        if valueDiff < 0:
            return False
        
        sorted_list = SortedList()

        for i, num in enumerate(nums):
            pos = sorted_list.bisect_left(num - valueDiff)
        
            if pos < len(sorted_list) and abs(sorted_list[pos] - num) <= valueDiff:
                return True
            
            sorted_list.add(num)

            if len(sorted_list) > indexDiff:
                sorted_list.remove(nums[i - indexDiff])

        return False

    # Brute Force
    def containsNearbyAlmostDuplicate_1(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        n = len(nums)

        for i in range(n):
            for j in range(n):
                if (
                    i != j
                    and abs(j - i) <= indexDiff
                    and abs(nums[i] - nums[j]) <= valueDiff
                ):
                    return True

        return False
