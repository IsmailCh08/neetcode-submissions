class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict()

        for i in range(len(nums)):
            number = target - nums[i]
            if number in hash:
                return [hash[number], i]
            else:
                hash[nums[i]] = i