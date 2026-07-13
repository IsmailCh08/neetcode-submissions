class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        window_length = len(s1)
        permutation, cur = {}, {}
        for char in s1:
            permutation[char] = permutation.get(char,0) + 1
        
        for right in range(len(s2)):
            char = s2[right]
            cur[char] = cur.get(char,0) + 1
            while right - left + 1 > window_length:
                cur[s2[left]] -= 1
                if cur[s2[left]] == 0:
                    cur.pop(s2[left])
                left += 1
            if right - left + 1 == window_length:
                if cur == permutation:
                    return True
        return False