class Solution:
    
    def maxScore(self, s: str) -> int:
        max_score = 0
        zero_score = 0
        ones_score = s.count('1')

        print(f"Ones: {ones_score}")

        for i in range(len(s) - 1):
            if s[i] == '0':
                zero_score += 1
            else:
                ones_score -= 1
            
            print(f"i: {i}, Ones: {ones_score}, zeros: {zero_score}")
            max_score = max(max_score, zero_score + ones_score)
            print(f"max: {max_score}")
        
        print(f"Ones: {ones_score}")
        print(f"Zero: {zero_score}")

        return max_score


    def maxScore2(self, s: str) -> int:
        total_ones = s.count("1")  # Count total number of 1s in the string
        left_zeros = 0
        max_score = 0

        for i in range(len(s) - 1):  # Split at index i (not including last character)
            if s[i] == "0":
                left_zeros += 1
            else:
                total_ones -= 1  # Removing 1 from right part
            
            max_score = max(max_score, left_zeros + total_ones)

        return max_score

    def maxScore_1(self, s: str) -> int:
        max_score = 0

        for i in range(len(s) - 1):
            right = i + 1

            zero_score = 0
            ones_score = 0
            left = 0
            while left < right:
                if s[left] == "0":
                    zero_score += 1
                left += 1

            while right < len(s):
                if s[right] == "1":
                    ones_score += 1
                right += 1

            max_score = max(max_score, zero_score + ones_score)

        return max_score
