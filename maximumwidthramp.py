
#A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

#Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

 

#Example 1:

#Input: nums = [6,0,8,2,1,5]
#Output: 4
#Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
#Example 2:

#Input: nums = [9,8,1,0,1,9,4,0,4,1]
#Output: 7
#Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.


#my brute force solution that got TLE 94/101:

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) -1, -1, -1):
            for j in range(i - 1, -1, -1):
                if nums[j] <= nums[i]:
                    res = max(res, i - j)
        return res


#corect python solution using montonic stack:

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        res = 0
        stack = []
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        for i in range(len(nums) -1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                idx = stack.pop()
                res = max(res, i - idx)
        return res
        
