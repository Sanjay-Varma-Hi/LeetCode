class Solution(object):
    def topKFrequent(self, nums, k):
            
        # 1. Count frequency (your exact logic)
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        # 2. Sort numbers by frequency (highest first)
        sorted_nums = sorted(freq, key=freq.get, reverse=True)

        # 3. Return first k numbers
        return sorted_nums[:k]