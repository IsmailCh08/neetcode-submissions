class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = dict()
    
        for i in range(len(nums)):
            num = nums[i]
            if num in hash:
                return True
            hash[num] = True
        return False