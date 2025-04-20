class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)

        def backtrack(current_string):

            if len(current_string) == n:
                if current_string not in nums:
                    return current_string
                else:
                    return None
            
            result = backtrack(current_string + '0')
            if result:
                return result
            
            result = backtrack(current_string + '1')

            if result:
                return result
            
            return None
            
        return backtrack("")