class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = right = 0
        max_window = 0
        replacements = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0 ) + 1
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            max_window = max(max_window,right-left+1)
        return max_window
            