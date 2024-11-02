
#2863
#medium

#You are given an integer array nums.

#Return the length of the longest semi-decreasing subarray of nums, and 0 if there are no such subarrays.

#A subarray is a contiguous non-empty sequence of elements within an array.
#A non-empty array is semi-decreasing if its first element is strictly greater than its last element.
 

#Example 1:

#Input: nums = [7,6,5,4,3,2,1,6,10,11]
#Output: 8
#Explanation: Take the subarray [7,6,5,4,3,2,1,6].
#The first element is 7 and the last one is 6 so the condition is met.
#Hence, the answer would be the length of the subarray or 8.
#It can be shown 


#correct python3 solution (could not solve):

class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        stack = []
        d = [0] * len(nums)
        for i in range(len(nums)):
            if not stack or nums[i] > nums[stack[-1]]:
                stack.append(i)
        for i in range(len(nums) -1, -1, -1):
            while stack and nums[i] < nums[stack[-1]]:
                idx = stack.pop()
                d[idx] = i - idx + 1
        return max(d)

        
