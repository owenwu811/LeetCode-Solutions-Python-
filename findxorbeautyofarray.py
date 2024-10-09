
#medium


#You are given a 0-indexed integer array nums.

#The effective value of three indices i, j, and k is defined as ((nums[i] | nums[j]) & nums[k]).

#The xor-beauty of the array is the XORing of the effective values of all the possible triplets of indices (i, j, k) where 0 <= i, j, k < n.

#Return the xor-beauty of nums.

#Note that:

#val1 | val2 is bitwise OR of val1 and val2.
#val1 & val2 is bitwise AND of val1 and val2.
 

#Example 1:

#Input: nums = [1,4]
#Output: 5
#Explanation: 
#The triplets and their corresponding effective values are listed below:
#- (0,0,0) with effective value ((1 | 1) & 1) = 1
#- (0,0,1) with effective value ((1 | 1) & 4) = 0
#- (0,1,0) with effective value ((1 | 4) & 1) = 1
#- (0,1,1) with effective value ((1 | 4) & 4) = 4
#- (1,0,0) with effective value ((4 | 1) & 1) = 1
#- (1,0,1) with effective value ((4 | 1) & 4) = 4
#- (1,1,0) with effective value ((4 | 4) & 1) = 0
#- (1,1,1) with effective value ((4 | 4) & 4) = 4 
#Xor-beauty of array will be bitwise XOR of all beauties = 1 ^ 0 ^ 1 ^ 4 ^ 1 ^ 4 ^ 0 ^ 4 = 5.



#my own solution using python3:

class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        result = nums[0]
        for i in range(1, len(nums)):
            result = result ^ nums[i]
        return result
