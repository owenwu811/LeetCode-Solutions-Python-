
#2393
#medium


#You are given an array nums consisting of positive integers.

#Return the number of subarrays of nums that are in strictly increasing order.

#A subarray is a contiguous part of an array.

 

#Example 1:

#Input: nums = [1,3,5,4,4,6]
#Output: 10
#Explanation: The strictly increasing subarrays are the following:
#- Subarrays of length 1: [1], [3], [5], [4], [4], [6].
#- Subarrays of length 2: [1,3], [3,5], [4,6].
#- Subarrays of length 3: [1,3,5].
#The total number of subarrays is 6 + 3 + 1 = 10.
#Example 2:

#Input: nums = [1,2,3,4,5]
#Output: 15
#Explanation: Every subarray is strictly increasing. There are 15 possible subarrays that we can take.


#my own different solution using python3 after looking at another solution:

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        l = 0
        for r in range(1, len(nums)):
            if nums[r] > nums[r - 1]:
                dp[r] += dp[r - 1]
        print(dp)
        return sum(dp)

