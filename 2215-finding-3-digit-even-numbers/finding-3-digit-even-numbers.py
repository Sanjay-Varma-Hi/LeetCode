class Solution(object):
    def findEvenNumbers(self, digits):
        from collections import Counter
        freq = Counter(digits)
        res = []
        for nums in range(100, 999, 2):
            parts = [nums // 100 , (nums // 10) % 10 , nums % 10]
            count = Counter(parts)
            if all(freq[d] >= count[d] for d in count):
                res.append(nums)
        return res
        
        