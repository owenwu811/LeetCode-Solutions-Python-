
#You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

#Return the sum of all the unique elements of nums.

#Input: nums = [1,2,3,2]
#Output: 4
#Explanation: The unique elements are [1,3], and the sum is 4.

#my own solution using python3:

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        res = 0
        d = dict()
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
        for k in d:
            if d[k] == 1:
                res += k
        return res
