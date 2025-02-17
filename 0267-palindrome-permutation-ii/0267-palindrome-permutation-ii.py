class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        freq = Counter(s)
        
        # Step 1: Check if palindrome permutation is possible
        odd_chars = [ch for ch in freq if freq[ch] % 2 == 1]
        if len(odd_chars) > 1:
            return []  # More than one odd character → cannot form a palindrome
        
        # Step 2: Prepare half-string and middle character
        half_chars = "".join(ch * (freq[ch] // 2) for ch in freq)
        mid_char = odd_chars[0] if odd_chars else ""
        
        # Step 3: Generate unique permutations of the half-string
        unique_permutations = set(permutations(half_chars))
        
        # Step 4: Construct full palindromes
        return ["".join(p) + mid_char + "".join(p[::-1]) for p in unique_permutations]



    def generatePalindromes2(self, s: str) -> List[str]:
        freq = Counter(s)

        odd_chars = [ch for ch in freq if freq[ch] % 2 == 1]
        if len(odd_chars) > 1:
            return [] 

        half_chars = []
        mid_char = odd_chars[0] if odd_chars else ""
        for ch, count in freq.items():
            half_chars.extend(
                [ch] * (count // 2)
            )  
        print(half_chars)

        def backtrack(start):
            if start == len(half_chars):
                result.append(
                    "".join(half_chars) + mid_char + "".join(half_chars[::-1])
                )
                return

            used = set()  # Track used characters at each level
            for i in range(start, len(half_chars)):
                if half_chars[i] in used:
                    continue  # Skip duplicate characters
                used.add(half_chars[i])

                # Swap and recurse
                half_chars[start], half_chars[i] = half_chars[i], half_chars[start]
                backtrack(start + 1)
                half_chars[start], half_chars[i] = (
                    half_chars[i],
                    half_chars[start],
                )  # Undo swap

        result = []
        backtrack(0)
        return result



    def generatePalindromes_1(self, s: str) -> List[str]:
        result = []
        s = sorted(s)
        visited = [False] * len(s)

        def isPalindrome(str):
            n = len(str)

            for i in range(n // 2):
                if str[i] != str[n - 1 - i]:
                    return False
            return True

        def backtrack(curr_str):
            if len(curr_str) == len(s):
                str2 = "".join(curr_str)
                if isPalindrome(str2):
                    result.append(str2)
                    return

            for i, ch in enumerate(s):
                if i > 0 and s[i] == s[i - 1] and not visited[i - 1]:
                    continue

                if not visited[i]:
                    visited[i] = True
                    curr_str.append(ch)
                    backtrack(curr_str)
                    visited[i] = False
                    curr_str.pop()

        backtrack([])
        return result
