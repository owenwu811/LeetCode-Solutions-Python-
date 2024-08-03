
#Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

#You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 
#Example 1:

#Input: nums = [1,2,1,3,2,5]
#Output: [3,5]
#Explanation:  [5, 3] is also a valid answer.
#Example 2:

#Input: nums = [-1,0]
#Output: [-1,0]
#Example 3:

#Input: nums = [0,1]
#Output: [1,0]


#my own solution in python3:

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        d = dict()
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
        for k in d:
            if d[k] == 1:
                res.append(k)
        return res
        
