
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        hours = 0
        min_eating_rate = 0
        while left <= right:
            hours = 0
            m = left + ((right-left)// 2)
            for pile in piles:
                hours += (pile + m - 1) // m
            if hours <= h:
                min_eating_rate = m
                right = m - 1
            else:
                left = m + 1
        return min_eating_rate