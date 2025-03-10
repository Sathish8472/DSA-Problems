class Solution:

    # Hashtable
    # Time: O(N), Space: O(N)
    def singleNumber(self, nums: List[int]) -> int:
        hashtable = defaultdict(int)

        for num in nums:
            hashtable[num] += 1
        
        for num in hashtable:
            if hashtable[num] == 1:
                return num
            
        return 0


    # Brute List operation
    # time: O(N * N), SpacE: O(N)
    def singleNumber_1(self, nums: List[int]) -> int:
        no_duplicate_list = []

        for num in nums:
            if num not in no_duplicate_list:            # time: O(N)
                no_duplicate_list.append(num)
            else:
                no_duplicate_list.remove(num)
        
        return no_duplicate_list.pop()

        