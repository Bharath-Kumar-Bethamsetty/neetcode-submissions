import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canEat(k):
            tm = 0
            for pile in piles:
                tm += math.ceil(pile/k)
            return tm <= h
        
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2
            if canEat(mid):
               right = mid - 1
            else:
                left = mid + 1
        
        return left