class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1.0
        
        if n == 1:
            return x
        
        if n < 0:
            return 1.0 / self.myPow(x, -n)

        if n % 2 == 0:
            half_pow = self.myPow(x, n // 2)
            return half_pow * half_pow
        else:
            return x * self.myPow(x, n - 1)
    
    def myPow1(self, x: float, n: int) -> float:
        if x == 1.0 or n == 0:
            return 1
            
        temp = n
        if n < 0:
            x = 1 / x
            temp = -1 * n

        ans = 1
        for i in range(temp):
            ans *= x
        
        return ans