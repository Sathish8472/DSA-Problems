class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for ch in s:
            stack.append(ch)

            if len(stack) >= k and stack[-k:] == [ch] * k:
                for _ in range(k):
                    stack.pop()
            
        return "".join(stack)
        