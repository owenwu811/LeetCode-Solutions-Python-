
#2873
#easy

#You are given a 0-indexed integer array nums.

#Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.

#The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].

 

#Example 1:

#Input: nums = [12,6,1,2,7]
#Output: 77
#Explanation: The value of the triplet (0, 2, 4) is (nums[0] - nums[2]) * nums[4] = 77.
#It can be shown that there are no ordered triplets of indices with a value greater than 77. 


#my own solution using python3:

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    res = max(res, (nums[i] - nums[j]) * nums[k])
        return res