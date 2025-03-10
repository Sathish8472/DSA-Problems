class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        no_duplicate_list = []

        for num in nums:
            if num not in no_duplicate_list:
                no_duplicate_list.append(num)
            else:
                no_duplicate_list.remove(num)
        
        return no_duplicate_list.pop()

        