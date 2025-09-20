class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.solve(0, 0, triangle)
    
    def solve(self, i, j, triangle):
        n = len(triangle)

        if i == n - 1:
            return triangle[i][j]

        if i >= len(triangle):
            return float('inf')
        
        if j < 0 or j >= len(triangle[i]):
            return float('inf')

        bottom = self.solve(i + 1, j, triangle)
        right_dg = self.solve(i + 1, j + 1, triangle)

        return triangle[i][j] + min(bottom, right_dg)