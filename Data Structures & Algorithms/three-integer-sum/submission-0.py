class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        for i,a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                three_Sum = a + nums[right] + nums[left]
                if three_Sum > 0:
                    right -= 1
                elif three_Sum < 0:
                    left += 1
                else:
                    result.append([a, nums[right],nums[left]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return result