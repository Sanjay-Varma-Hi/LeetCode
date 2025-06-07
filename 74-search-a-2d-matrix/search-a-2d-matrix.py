class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        flattened = [item for sublist in matrix for item in sublist]
        for i in range(0,len(flattened)):
            if flattened[i] == target:
                return True
        return False