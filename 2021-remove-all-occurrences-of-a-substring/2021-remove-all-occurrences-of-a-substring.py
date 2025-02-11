class Solution:

    # Efficient Stack Approach
    # Time: O(N), Space: O(N)
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []

        for ch in s:
            stack.append(ch)

            # Check if the top len(part) characters form part
            if len(stack) >= len(part) and "".join(stack[-len(part) :]) == part:
                del stack[-len(part) :]

        return "".join(stack)




    # Brute Force
    # Time: O(N * M)
    # Space: O(N)
    def removeOccurrences_1(self, s: str, part: str) -> str:
        
        while part in s:
            index = s.find(part)  # O(M) time taken
            s = s[:index] + s[index + len(part) :]     # Extra Space for slicing

        return s
