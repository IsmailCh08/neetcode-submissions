class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        water = 0
        left_max = height[left]
        right_max = height[right]
        while left <= right:
                if left_max < right_max:
                    left_max = max(height[left],left_max)
                    water += max(0,left_max - height[left])
                    left += 1
                else:
                    right_max = max(height[right],right_max)
                    water += max(0,right_max - height[right])
                    right -= 1
        return water