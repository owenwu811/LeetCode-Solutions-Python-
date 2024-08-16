
#You are given an array nums consisting of positive integers.

#Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

#The frequency of an element is the number of occurrences of that element in the array.

#Input: nums = [1,2,2,3,1,4]
#Output: 4
#Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
#So the number of elements in the array with maximum frequency is 4.

#my own solution using python3:

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = dict()
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
        ma = 0
        for k in d:
            ma = max(ma, d[k])
        res = 0
        for n in nums:
            if d[n] == ma:
                res += 1
        return res
