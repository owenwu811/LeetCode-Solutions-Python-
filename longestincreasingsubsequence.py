
#Given an integer array nums, return the length of the longest strictly increasing 
#subsequence

#Input: nums = [10,9,2,5,3,7,101,18]
#Output: 4
#Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

#python3 solution:

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1] * len(nums) #1 because we can just choose itself as longest atleast 1
        for i in range(len(nums) -1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]: #j is in front of i always since we want longest increasing sequence
                    res[i] = max(res[i], 1 + res[j])
        return max(res)

