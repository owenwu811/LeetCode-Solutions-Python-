#2148
#easy
#59.9% acceptance rate


#Given an integer array nums, return the number of elements that have both a strictly smaller and a strictly greater element appear in nums.

 

#Example 1:

#Input: nums = [11,7,2,15]
#Output: 2
#Explanation: The element 7 has the element 2 strictly smaller than it and the element 11 strictly greater than it.
#Element 11 has element 7 strictly smaller than it and element 15 strictly greater than it.
#In total there are 2 elements having both a strictly smaller and a strictly greater element appear in nums.




#my own solution using python3:

class Solution:
    def countElements(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            if n == max(nums) or n == min(nums):
                continue
            else:
                res += 1
        return res
