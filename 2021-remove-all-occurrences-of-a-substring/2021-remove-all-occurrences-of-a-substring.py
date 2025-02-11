class Solution:
    def removeOccurrences_1(self, s: str, part: str) -> str:
        stack = []

        for ch in s:
            stack.append(ch)

            if len(stack) >= len(part) and "".join(stack[-len(part) :]) == part:
                del stack[-len(part) :]

        return "".join(stack)
    


    # Brute Force
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            index = s.find(part)
            s = s[:index] + s[index + len(part):]

        return s