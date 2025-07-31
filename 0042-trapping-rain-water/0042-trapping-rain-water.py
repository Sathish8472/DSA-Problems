class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = right_max = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1

        return water




    # Better, T: O(3N), S: O(3N)
    def trap1(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i]) 
        
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
        water = 0
        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]
        
        return water



    # Brute - T: O(N ^ 2), Space: O(1)
    def trap1(self, height: List[int]) -> int:
        n = len(height)

        water = 0

        for i in range(n):
            left = max(height[:i + 1])
            right = max(height[i: ])

            water += min(left, right) - height[i]
        
        return water
        