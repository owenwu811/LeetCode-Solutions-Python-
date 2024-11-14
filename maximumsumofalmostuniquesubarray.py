
#2841
#medium

#You are given an integer array nums and two positive integers m and k.

#Return the maximum sum out of all almost unique subarrays of length k of nums. If no such subarray exists, return 0.

#A subarray of nums is almost unique if it contains at least m distinct elements.

#A subarray is a contiguous non-empty sequence of elements within an array.

 

#Example 1:

#Input: nums = [2,6,7,3,1,7], m = 3, k = 4
#Output: 18
#Explanation: There are 3 almost unique subarrays of size k = 4. These subarrays are [2, 6, 7, 3], [6, 7, 3, 1], and [7, 3, 1, 7]. Among these subarrays, the one with the maximum sum is [2, 6, 7, 3] which has a sum of 18


#my own solution using python3:

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        res = 0
        for i in range(len(nums) - k + 1):
            subarr = nums[i: i + k]
            if len(set(subarr)) >= m:
                res = max(res, sum(subarr))
        return res
