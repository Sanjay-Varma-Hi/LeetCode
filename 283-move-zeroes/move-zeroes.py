class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last_non_zero = 0  # Pointer to track the position to place the next non-zero element
        
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap the non-zero element to the 'last_non_zero' position
                nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
                last_non_zero += 1
        
        # No need to return anything, the array is modified in place
