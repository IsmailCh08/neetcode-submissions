class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        permutation = {}
        permutation_check = {}
        left = 0
        right = 0
        for char in s1:
            permutation[char] = permutation.get(char, 0) + 1
        
        for char in s2:
            permutation_check[char] = permutation_check.get(char,0) + 1
            while right - left + 1 == len(s1):
                if permutation == permutation_check:
                    return True
                else:
                    permutation_check[s2[left]] -= 1
                    if permutation_check[s2[left]] == 0:
                        permutation_check.pop(s2[left])
                    left += 1
            right += 1
        return False
