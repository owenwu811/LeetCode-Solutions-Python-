

#1063
#hard

#Given an integer array nums, return the number of non-empty subarrays with the leftmost element of the subarray not larger than other elements in the subarray.

#A subarray is a contiguous part of an array.

 

#Example 1:

#Input: nums = [1,4,2,5,3]
#Output: 11
#Explanation: There are 11 valid subarrays: [1],[4],[2],[5],[3],[1,4],[2,5],[1,4,2],[2,5,3],[1,4,2,5],[1,4,2,5,3].
#Example 2:

#Input: nums = [3,2,1]
#Output: 3
#Explanation: The 3 valid subarrays are: [3],[2],[1].
#Example 3:

#Input: nums = [2,2,2]
#Output: 6
#Explanation: There are 6 valid subarrays: [2],[2],[2],[2,2],[2,2],[2,2,2].


#correct python3 solution (could not solve):

class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(nums)):
            while stack and nums[i] < nums[stack[-1]]:
                a = stack.pop() 
            stack.append(i)
            res += len(stack) 
        return res
