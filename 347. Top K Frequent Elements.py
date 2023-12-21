class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        freq = [[] for i in range(len(nums)+1)]

        # adding no as key and value as number of occurences
        for n in nums: d[n] = 1 + d.get(n, 0)

        # storing value at index in array(e.g at index 1 if it occures once)
        for n, c in d.items(): freq[c].append(n)

        # res array to return later
        res = []
        # iterate in reverse order
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                # when at any point, len(res) == k, return res
                # as we want top k elements
                if len(res) == k: return res
        
        