
#Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

#Example 1:

#Input: nums = [3,2,3]
#Output: [3]
#Example 2:

#Input: nums = [1]
#Output: [1]
#Example 3:

#Input: nums = [1,2]
#Output: [1,2]


#my solution in Python3:

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mydict = defaultdict(int)
        res = []
        number = len(nums) / 3
        for n in nums:
            mydict[n] += 1
        for d in mydict:
            if mydict[d] > number:
                res.append(d)
        return res
