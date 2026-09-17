class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = {}
        t_letters = {}
        if len(t) != len(s):
            return False
        for i in range(len(s)):
            s_letters[s[i]] = s_letters.get(s[i],0) + 1
            t_letters[t[i]] = t_letters.get(t[i],0) + 1
        return s_letters == t_letters