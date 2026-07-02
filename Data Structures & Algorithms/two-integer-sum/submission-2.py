class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict()

        for i in range(len(nums)):
            num = nums[i]
            needed = target - num
            if needed in hash:
                return [hash[needed], i]
            else:
                hash[num] = i