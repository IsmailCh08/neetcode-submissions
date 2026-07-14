class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count, s_count = {}, {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        have = 0
        need = len(t_count)
        left = 0
        right = 0
        res_len = float('inf')
        res = [-1,-1]
        for char in s:
            s_count[char] = s_count.get(char,0) + 1

            if char in t_count and s_count[char] == t_count[char]:
                have += 1

            while have == need:
                if res_len > right - left + 1:
                    res_len = right - left + 1
                    res = [left,right]
                s_count[s[left]] -= 1
                if s[left] in t_count and s_count[s[left]] < t_count[s[left]]:
                    have -= 1
                if s_count[s[left]] == 0:
                    s_count.pop(s[left])
                left += 1
            right += 1
        left, right = res
        return s[left:right+1]