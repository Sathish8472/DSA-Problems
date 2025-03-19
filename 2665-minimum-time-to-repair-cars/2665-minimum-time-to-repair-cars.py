class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left, right = 1, min(ranks) * cars * cars

        def canRepairInTime(time_limit):
            total_cars = sum(int(math.sqrt(time_limit // r)) for r in ranks)
            return total_cars >= cars
        
        while left < right:
            mid = (left + right) // 2
            if canRepairInTime(mid):
                right = mid
            else:
                left = mid + 1
            
        return left
        