#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

#You must write an algorithm that runs in O(n) time.

 

#Example 1:

#Input: nums = [100,4,200,1,3,2]
#Output: 4
#Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
#Example 2:

#Input: nums = [0,3,7,2,5,8,4,6,0,1]
#Output: 9


#my Solution (python3) - 11/7/23:

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res, maxres = 0, 0
        nums.sort()
        for i in range(len(nums)): #0123456789
            if i > 0 and nums[i] == nums[i - 1]: #
                maxres = max(maxres, res)
                continue
            if i > 0 and nums[i] > nums[i - 1] + 1: #we found a breakpoint, so continue
                maxres = max(maxres, res)
                res = 0
            res += 1
        return max(maxres, res)
