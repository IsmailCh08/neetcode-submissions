class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_water = water = 0
        while left < right:
            water = (right - left) * min(heights[right],heights[left])
            max_water = max(max_water,water)
            if heights[right] > heights[left]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                right -= 1
        return max_water