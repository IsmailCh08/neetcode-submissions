class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for number in nums:
            count[number] = count.get(number,0) + 1
        freq = [[] for _ in range(len(nums)+1)]
        for num, freq_count in count.items():
            freq[freq_count].append(num)
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        