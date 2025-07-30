class Solution:
    def removeDuplicateLetters1(self, s: str) -> str:
        
        alphabets = [0] * 26

        for ch in s:
            index = ord(ch) - ord('a')
            alphabets[index] = 1

        result = ""
        for i in range(26):
            if alphabets[i]:
                result += chr(i + ord('a'))

        return result
                
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        count = {ch: 0 for ch in s}

        for ch in s:
            count[ch] += 1

        for ch in s:
            count[ch] -= 1
            if ch in seen:
                continue

            while stack and ch < stack[-1] and count[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(ch)
            seen.add(ch)

        return ''.join(stack)
