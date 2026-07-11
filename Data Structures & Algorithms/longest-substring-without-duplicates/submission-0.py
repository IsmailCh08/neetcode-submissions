class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()
        left = 0
        right = 0
        max_count = 0
        for i in range(len(s)):
            while s[i] in count:
                count.remove(s[left])
                left += 1
            else:
                count.add(s[i])
                right += 1
                max_count = max(max_count,right-left)
        return max_count