#Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

#You must implement a solution with a linear runtime complexity and use only constant extra space.

#Example 1:

#Input: nums = [2,2,3,2]
#Output: 3
#Example 2:

#Input: nums = [0,1,0,1,0,1,99]
#Output: 99


#my solution in python3:

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mydict = dict()
        for n in nums:
            if n not in mydict:
                mydict[n] = 0
            mydict[n] += 1
        for d in mydict:
            if mydict[d] > 1:
                continue
            else:
                return d



