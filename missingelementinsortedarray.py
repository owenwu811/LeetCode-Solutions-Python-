

#1060
#medium

#Given an integer array nums which is sorted in ascending order and all of its elements are unique and given also an integer k, return the kth missing number starting from the leftmost number of the array.

 

#Example 1:

#Input: nums = [4,7,9,10], k = 1
#Output: 5
#Explanation: The first missing number is 5.
#Example 2:

#Input: nums = [4,7,9,10], k = 3
#Output: 8
#Explanation: The missing numbers are [5,6,8,...], hence the third missing number is 8.
#Example 3:

#Input: nums = [1,2,4], k = 3
#Output: 6
#Explanation: The missing numbers are [3,5,6,7,...], hence the third missing number is 6.


#correct python3 solution (could not solve):

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] - min(nums) - mid < k:
                l = mid + 1
            else:
                r = mid - 1
        return l + nums[0] + k - 1
