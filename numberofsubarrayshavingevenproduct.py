#2495
#medium

#Given a 0-indexed integer array nums, return the number of 
#subarrays
# of nums having an even product.

 

#Example 1:

#Input: nums = [9,6,7,13]
#Output: 6
#Explanation: There are 6 subarrays with an even product:
#- nums[0..1] = 9 * 6 = 54.
#- nums[0..2] = 9 * 6 * 7 = 378.
#- nums[0..3] = 9 * 6 * 7 * 13 = 4914.
#- nums[1..1] = 6.
#- nums[1..2] = 6 * 7 = 42.
#- nums[1..3] = 6 * 7 * 13 = 546.
#Example 2:

#Input: nums = [7,3,5]
#Output: 0
#Explanation: There are no subarrays with an even product.


#my naive solution only passing 24/53 test cases:

class Solution:
    def evenProduct(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarr = nums[i: j + 1]
                if math.prod(subarr) % 2 == 0:
                    res += 1
        return res


#correct python3 solution (could not solve):

class Solution:
    def evenProduct(self, nums: List[int]) -> int:
        res = 0
        cur = -1 #declaring last even as -1 because you will add + 1 to the current index if we see an even number because -1 + 1 = 0
        for i, n in enumerate(nums):
            if n % 2 == 0:
                cur = i #a subarray's product becomes even as soon as it includes even one even number       
            res += (cur + 1)
        return res
