#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

#You must implement a solution with a linear runtime complexity and use only constant extra space.

#Input: nums = [2,2,1]
#Output: 1


#my solution - python3:

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mydict = dict()
        res = 0
        for number in nums:
            if number not in mydict:
                mydict[number] = 0
            mydict[number] += 1
        for d in mydict:
            if mydict[d] > 1:
                continue
            res = d
        return res
            
