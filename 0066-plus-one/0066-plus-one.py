class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0
        
        return [1] + digits






    def plusOne1(self, digits: List[int]) -> List[int]:

        carry = 1
        n = len(digits)
        result = []

        for i in range(n - 1, -1, -1):
            num = digits[i]
            if num + carry == 10:
                num = 0
            else:
                num = num + carry
                carry = 0

            result.append(num)
        
        if carry == 1:
            result.append(1)
        
        print(result)
        return result[::-1]
        