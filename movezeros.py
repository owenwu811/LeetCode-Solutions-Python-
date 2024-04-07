
#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

#Note that you must do this in-place without making a copy of the array.

#nums = [0,1,0,3,12]
#output: [1,3,12,0,0]


#python3 solution:

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #[0, 1, 0, 3, 12]
        #[1, 0, 0, 3, 12]
        #[1, 0, 3, 0, 12]
        #[1, 3, 0, 0, 12]
        #[1, 3, 0, 12, 0]
        #[1, 3, 12, 0, 0]
        slow = 0
        for fast in range(1, len(nums)):
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            elif nums[slow] != 0:
                slow += 1
        
