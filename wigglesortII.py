#Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

#You may assume the input array always has a valid answer.

 

#Example 1:

#Input: nums = [1,5,1,1,6,4]
#Output: [1,6,1,5,1,4]
#Explanation: [1,4,1,5,1,6] is also accepted.

#note that nums[::2] for nums = [1, 2, 3, 4, 5] = [1, 3, 5] (indexes 0, 2, 4)
#note that nums[1::2] for nums = [1, 2, 3, 4, 5] = [2, 4] (indexes 1 and 3)


#python3 solution:

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums) #6 > [1, 5, 1, 1, 6, 4]
        nums.sort() #[1, 1, 1, 4, 5, 6]
        mid = (n - 1) // 2 #2 (because (6 - 1) // 2 = 5 // 2 = 2)
        nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1] #nums[::2] = [1, 1, 5] (indexes 0, 2, 4), nums[1::2] = [1, 4, 6] (indexes 1, 3, 5), and nums[mid::-1] = [1, 1, 1] (1st half of list) and nums[:mid:-1] = [6, 5, 4] (reversed 2nd half of list)
