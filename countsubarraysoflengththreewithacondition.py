#3392
#easy

#Given an integer array nums, return the number of 
#subarrays
# of length 3 such that the sum of the first and third numbers equals exactly half of the second number.

 

#Example 1:

#Input: nums = [1,2,1,4,1]

#Output: 1

#Explanation:

#Only the subarray [1,4,1] contains exactly 3 elements where the sum of the first and third numbers equals half the middle number.


#my own solution using python3:

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) - 2):
            subarr = nums[i: i + 3]
            print(subarr)
            if subarr[0] + subarr[2] == subarr[1] / 2:
                res += 1
        return res
