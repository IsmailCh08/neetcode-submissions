class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_anag, t_anag = {}, {}
        for i in range(len(s)):
            s_anag[s[i]] = s_anag.get(s[i], 0) +1
            t_anag[t[i]] = t_anag.get(t[i], 0) +1
        return s_anag == t_anag