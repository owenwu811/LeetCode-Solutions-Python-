#2913
#easy

#You are given a 0-indexed integer array nums.

#The distinct count of a subarray of nums is defined as:

#Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
#Return the sum of the squares of distinct counts of all subarrays of nums.

#A subarray is a contiguous non-empty sequence of elements within an array.

 

#Example 1:

#Input: nums = [1,2,1]
#Output: 15

#The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15


#my own solution using python3:

#just get all subarrays and then count the numebr of distinct elements, square that number, and add all of these numbers up

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarr = nums[i: j + 1]
                distinct = len(set(subarr))
                res += (distinct * distinct)
        return res
