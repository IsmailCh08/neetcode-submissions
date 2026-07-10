class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        results = []
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                total = nums[l]+nums[r]+a
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    results.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return results
