class Solution:

    # Min-heap
    # Time:  O(N + N log N) = O(N log N)
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)         # O(N)

        num_operations = 0
        while nums[0] < k:
            x = heapq.heappop(nums)    # O(log N)
            y = heapq.heappop(nums)    # O(log N)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))     # O(log N)

            num_operations += 1

        return num_operations
        


    # Brute Force
    # In the worst case, each iteration reduces the size of the array only slightly because the new element (min1 * 2 + min2) can still be smaller than k.
    # O(N ^ 2)
    def minOperations_1(self, nums: List[int], k: int) -> int:
        count = 0

        while True:
            
            if all(num >= k for num in nums):   # O(N)
                return count

            min1 = float("inf")
            min2 = float("inf")

            for num in nums:                # O(N)
                if num < min1:
                    min2 = min1
                    min1 = num
                elif num < min2:
                    min2 = num

            nums.remove(min1)               # O(N)
            nums.remove(min2)               # O(N)

            val = min1 * 2 + min2
            nums.append(val)                # O(1)
            count += 1
            print(count)

            
