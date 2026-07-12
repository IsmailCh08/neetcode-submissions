class Solution:
    def minWindow(self, s: str, t: str) -> str:
        substring = {}
        window_count = {}
        for char in t:
            substring[char] = substring.get(char, 0) + 1
        need = len(substring)
        have = 0
        res = ""
        res_len = float('inf')
        left = 0
        for r in range(len(s)):
            window_count[s[r]] = window_count.get(s[r], 0) + 1
            if s[r] in substring:
                if window_count[s[r]] == substring[s[r]]:
                    have += 1
            
            while have == need:
                if len(s[left:r+1]) < res_len:
                    res = s[left:r+1]
                    res_len = len(res)
                window_count[s[left]] -= 1
                char = s[left]
                if char in substring and window_count[s[left]] < substring[s[left]]:
                    have -= 1
                left += 1
        return res
            

