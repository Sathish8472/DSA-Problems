class Solution:

    # Two-Pointer Approach (Iterative)
    def isSubsequence_1(self, s: str, t: str) -> bool:
        index = 0

        for ch in t:
            if index < len(s) and s[index] == ch:
                index += 1

        return index == len(s)


    def isSubsequence(self, s: str, t: str) -> bool:
        t_iter = iter(t)
        return all(char in t_iter for char in s)


    # Can be solved using DP, Recursive, Binary Search and others