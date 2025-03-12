class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0

        for i in range(len(s) - 1):
            right = i + 1

            zero_score = 0
            ones_score = 0
            left = 0
            while left < right:
                if s[left] == '0':
                    zero_score += 1
                left += 1
            
            while right < len(s):
                if s[right] == '1':
                    ones_score += 1
                right += 1
            
            print(zero_score, ones_score)
            
            max_score = max(max_score, zero_score + ones_score)

        return max_score
        