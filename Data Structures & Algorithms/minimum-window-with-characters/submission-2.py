class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        substring , cur_letter = {}, {}
        left = 0
        res = [-1,-1]
        result_len = float('inf')
        for char in t:
            substring[char] = substring.get(char,0) + 1
        need = len(substring)
        have = 0
        for right in range(len(s)):
            cur_letter[s[right]] = cur_letter.get(s[right], 0 )+ 1
            if s[right] in substring and cur_letter[s[right]] == substring[s[right]]:
                have += 1
            
            while have == need:
                if right - left + 1 < result_len:
                    result_len = right - left + 1
                    res = [left,right]
                cur_letter[s[left]] -= 1
                if s[left] in substring and cur_letter[s[left]] < substring[s[left]]:
                    have -= 1
                left += 1
        left,right = res
        return s[left:right+1]
