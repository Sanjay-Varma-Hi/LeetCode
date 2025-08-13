class Solution(object):
    def searchMatrix(self, matrix, target):
        flat = [num for row in matrix for num in row]
        flat.sort()
        l,r=0,len(flat)-1

        while l<=r:
            m=(l+r)//2
            if flat[m]==target:
                return True
            elif flat[m] < target:
                l=m+1
            else:
                r=m-1
        