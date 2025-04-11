class Solution:

    # time: O(high - low)
    # space: constant
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        count = 0
        for i in range(low, high + 1):
            num_str = str(i)
            num_len = len(num_str)
            if num_len % 2 == 0 and self._divide_numbers_check_sum(num_str, num_len):
                count += 1
        
        return count

    
    def _divide_numbers_check_sum(self, num_str,num_len ):

        first_sum = 0 
        second_sum = 0 

        left = 0
        right = num_len - 1

        while left < right:
            first_sum += int(num_str[left])
            second_sum += int(num_str[right])
            left += 1
            right -= 1

        return first_sum == second_sum


