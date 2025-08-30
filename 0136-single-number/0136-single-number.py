class Solution:

    # Bit manipulation
    # Time: O(N), Space: O(1)
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a


    # Math 
    # Time: O(N), SpacE: O(N)
    def singleNumber_3(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)               # T: O(N + N), S: O(N)



    # Hashtable
    # Time: O(N), Space: O(N)
    def singleNumber_2(self, nums: List[int]) -> int:
        hashtable = defaultdict(int)

        for num in nums:
            hashtable[num] += 1
        
        for num in hashtable:
            if hashtable[num] == 1:
                return num
            
        return 0
        