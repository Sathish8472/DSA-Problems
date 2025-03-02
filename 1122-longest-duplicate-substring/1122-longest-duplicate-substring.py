class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def rabin_karp(L):
            """Returns the starting index of a duplicate substring of length L using Rabin-Karp hashing, or -1 if none exists."""
            q = 2**63 - 1  # Large prime modulus
            d = 26  # Number of characters (a-z)
            n = len(s)
            
            # Compute hash for first substring of length L
            h = 0
            for i in range(L):
                h = (h * d + ord(s[i]) - ord('a')) % q
            seen = {h}  # Store the hashes
            
            # Rolling hash: Precompute (d^L) % q to remove old character efficiently
            dL = pow(d, L, q)
            
            # Check all other substrings
            for i in range(1, n - L + 1):
                # Compute new hash by removing left character and adding right character
                h = (h * d - (ord(s[i - 1]) - ord('a')) * dL + ord(s[i + L - 1]) - ord('a')) % q
                
                if h in seen:
                    return i  # Found a duplicate
                seen.add(h)
            
            return -1  # No duplicate found
    
        # Binary search for the longest duplicate substring
        left, right = 1, len(s)
        start_idx, max_len = -1, 0
        
        while left < right:
            mid = (left + right) // 2
            idx = rabin_karp(mid)
            
            if idx != -1:
                start_idx, max_len = idx, mid
                left = mid + 1  # Try a longer length
            else:
                right = mid  # Try a shorter length
        
        return s[start_idx:start_idx + max_len] if start_idx != -1 else ""