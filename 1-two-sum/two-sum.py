class Solution(object):
    def twoSum(self, nums, target):
      
        arr = [(n, i) for i, n in enumerate(nums)]
        arr.sort()  # sort by value

        left, right = 0, len(arr) - 1

        while left < right:
            s = arr[left][0] + arr[right][0]
            if s == target:
                return [arr[left][1], arr[right][1]]
            elif s < target:
                left += 1
            else:
                right -= 1

        return None