class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char)-ord('a')] += 1
            hash[tuple(count)].append(string)
        return list(hash.values())