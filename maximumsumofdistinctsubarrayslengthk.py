

#2461
#medium
#34.2% acceptance rate


#You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

#The length of the subarray is k, and
#All the elements of the subarray are distinct.
#Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

#A subarray is a contiguous non-empty sequence of elements within an array.

 

#Example 1:

#Input: nums = [1,5,4,2,9,9,9], k = 3
#Output: 15
#Explanation: The subarrays of nums with length 3 are:
#- [1,5,4] which meets the requirements and has a sum of 10.
#- [5,4,2] which meets the requirements and has a sum of 11.
#- [4,2,9] which meets the requirements and has a sum of 15.
#- [2,9,9] which does not meet the requirements because the element 9 is repeated.
#- [9,9,9] which does not meet the requirements because the element 9 is repeated.
#We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions




#my own brute force solution using python3 63/93 TLE:

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        for i in range(len(nums) - k + 1):
            window = nums[i: i + k]
            if len(set(window)) == k:
                res = max(res, sum(window))
        return res



#my own correct python3 solution after looking at the solution:

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d = dict()
        res = 0
        cursum = 0
        l = 0
        for r in range(len(nums)):
            cursum += nums[r]
            if nums[r] not in d: #we add the incoming number to the dictionary, not the cursum because we want to use the length of the dictionary later to see if there are any duplicates, so the dictionary represents the state of the window itself
                d[nums[r]] = 1
            else:
                d[nums[r]] += 1
            if (r - l + 1) == k: #hit our limit windowsize of k
                if len(d) == k: #no duplicates because how many dictionary key's we have represents the length of our window
                    res = max(res, cursum)
                #we only shrink the window once we have hit our size of k
                cursum -= nums[l]
                d[nums[l]] -= 1
                if d[nums[l]] == 0:
                    del d[nums[l]]
                l += 1
        return res
