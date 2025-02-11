class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []

        for ch in s:
            stack.append(ch)

            if len(stack) >= len(part) and "".join(stack[-len(part) :]) == part:
                del stack[-len(part) :]

        return "".join(stack)
