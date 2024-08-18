#Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

#Example 1:

#Input: nums = [10,5,2,6], k = 100
#Output: 8
#Explanation: The 8 subarrays that have product less than 100 are:
#[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
#Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
#Example 2:

#Input: nums = [1,2,3], k = 0
#Output: 0


#my own solution after some guidance using python3:

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        r = 0
        curprod = 1
        l = 0
        while r < len(nums):
            if nums[r] == 0:
                curprod = 1
                r += 1
                continue
            curprod *= nums[r]
            if curprod < k:
                res += (r - l + 1) #key finding is that the number of subarrays is actually the exact length of the window, so by introducing 2 to [10, 5] to become [10, 5, 2], we introduce 3 new subarrays because [10, 5, 2] is of length 3! r and l are indicies, so + 1 is needed!
            while curprod >= k and l <= r: #need to use while loop here because as long as we are over or equal to k, we have to keep shrinking the window! and l <= r because window wouldn't be equal to anything
                curprod = curprod / nums[l]
                l += 1
                if curprod < k:
                    res += (r - l + 1)
            r += 1
        return res
