
#1005
#easy

#Given an integer array nums and an integer k, modify the array in the following way:

#choose an index i and replace nums[i] with -nums[i].
#You should apply this process exactly k times. You may choose the same index i multiple times.

#Return the largest possible sum of the array after modifying it in this way.

 

#Example 1:

#Input: nums = [4,2,3], k = 1
#Output: 5
#Explanation: Choose index 1 and nums becomes [4,-2,3].


#my own solution using python3:

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        while k > 0:
            nums[0] *= -1
            nums.sort()  
            k -= 1
        return sum(nums)

        
