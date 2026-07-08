class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        
        nums = set(nums)
        longest = max_length = 1
        for num in nums:
            longest = 1
            if (num - 1) not in nums:
                while (num + 1) in nums:
                    longest += 1
                    max_length = max(longest,max_length)
                    num += 1
        return max_length



