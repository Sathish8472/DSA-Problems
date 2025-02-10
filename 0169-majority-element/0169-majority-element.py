class Solution:
    # Boyer-Moore Voting Algorithm
    # time: O(N), Space: O(1)
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            # Increment count if the current number is candidate, else decrement it
            count += (1 if candidate == num else -1)

        return candidate




    # Sorting
    def majorityElement_3(self, nums: List[int]) -> int:
        nums.sort()             # cost n logn 
        return nums[len(nums) // 2]



    # HashMap with built-in
    # Time: O(N), Space: O(N)
    def majorityElement_2(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        print(counts)
        return max(counts.keys(), key = counts.get)



    # Brute force, Time: O(N ^ 3)
    def majorityElement_1(self, nums: List[int]) -> int:
        majority_count = len(nums) // 2
        
        for num in nums:
            count = sum(1 for element in nums if element == num) # takes O(N) for each iteration
            if count > majority_count:
                return num