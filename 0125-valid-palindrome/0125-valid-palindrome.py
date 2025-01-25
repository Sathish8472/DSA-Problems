class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = ''.join(c.lower() for c in s if c.isalnum())  # this is filtering the special characters
        n = len(filtered_chars)
        
        for i in range(n // 2):
            if(filtered_chars[i] != filtered_chars[n - 1 - i]):
                return False;

        return True;
        

# Two pointer solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = ''.join(c.lower() for c in s if c.isalnum())  # this is filtering the special characters
        print("dsfsd")
        left, right = 0, len(filtered_chars) - 1
        while(left < right):
            if(filtered_chars[left] != filtered_chars[right]):
                return False
            left += 1
            right -= 1

        return True