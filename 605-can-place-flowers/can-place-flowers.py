class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        length = len(flowerbed)
        if n==0:
            return True
        for i in range(length):
            if flowerbed[i] == 0:
                empty_prev = (i == 0) or (flowerbed[i - 1] == 0)
                empty_next = (i == length - 1) or (flowerbed[i + 1] == 0)
            
                if empty_prev and empty_next:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
        return n == 0
