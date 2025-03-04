class Solution:

    # Bucket Sort (HashMap)
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False

        bucket = {}  # Dictionary to store elements in buckets
        bucket_size = valueDiff + 1  # Size of each bucket

        for i, num in enumerate(nums):
            bucket_key = num // bucket_size

            # Check if the current bucket already has an element
            if bucket_key in bucket:
                return True
            
            # Check adjacent buckets for close elements
            if bucket_key - 1 in bucket and abs(num - bucket[bucket_key - 1]) <= valueDiff:
                return True
            if bucket_key + 1 in bucket and abs(num - bucket[bucket_key + 1]) <= valueDiff:
                return True

            # Insert current number into its bucket
            bucket[bucket_key] = num

            # Maintain window size by removing old elements
            if i >= indexDiff:
                del bucket[nums[i - indexDiff] // bucket_size]

        return False


    # SortedList (Binary Search)
    def containsNearbyAlmostDuplicate2(self, nums: List[int], indexDiff: int, valueDiff: int):

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
