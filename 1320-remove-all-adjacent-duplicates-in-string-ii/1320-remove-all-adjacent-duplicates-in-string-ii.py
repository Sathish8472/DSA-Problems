class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        count = 0

        for ch in s:

            if stack:
                print("Stack -1: ", stack[-1][0])

            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([ch, 1])
        
        print("stack: ", stack)
        result = ""
        for ch, count in stack:
            result += ch * count

        return result