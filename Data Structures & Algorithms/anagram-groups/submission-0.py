class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = dict()
        for i in range(len(strs)):
            sorted_string = ''.join(sorted(strs[i]))
            if sorted_string in hash:
                hash[sorted_string].append(strs[i])
            else:
                hash[sorted_string] = [strs[i]]
        return list(hash.values())