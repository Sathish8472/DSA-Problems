class Solution:
    def findPermutation(self, s: str) -> List[int]:
        stack = []
        i = 1
        result = []

        for ch in s:
            if ch == "I":
                stack.append(i)
                while stack:
                    result.append(stack.pop())
            else:
                stack.append(i)
            i += 1

        stack.append(i)
        while stack:
            result.append(stack.pop())

        return result





        