class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = i = 0
        special_substrings = []
        
        # Identify special substrings
        for j in range(len(s)):
            count += 1 if s[j] == '1' else -1
            if count == 0:  # Found a special substring
                # Recursively process the inner substring
                special_substrings.append('1' + self.makeLargestSpecial(s[i + 1:j]) + '0')
                i = j + 1  # Move to the next potential special substring

        # Sort the special substrings in descending order
        special_substrings.sort(reverse=True)
        
        # Join them to form the final result
        return ''.join(special_substrings)

# Example usage
solution = Solution()
s1 = "11011000"
print(solution.makeLargestSpecial(s1))  # Output: "11100100"

s2 = "10"
print(solution.makeLargestSpecial(s2))  # Output: "10"
