
#2815
#easy

#You are given an integer array nums. You have to find the maximum sum of a pair of numbers from nums such that the largest digit in both numbers is equal.

#For example, 2373 is made up of three distinct digits: 2, 3, and 7, where 7 is the largest among them.

#Return the maximum sum or -1 if no such pair exists.

 

#Example 1:

#Input: nums = [112,131,411]

#Output: -1

#Explanation:

#Each numbers largest digit in order is [2,3,4].



#my own solution using python3:

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                first = str(nums[i])
                second = str(nums[j])
                a = max(first)
                b = max(second)
                if a == b:
                    res = max(res, nums[i] + nums[j])
        if res == 0:
            return -1
        return res
