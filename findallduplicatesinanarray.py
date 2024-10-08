

#Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

#You must write an algorithm that runs in O(n) time and uses only constant extra space.

 

#Example 1:

#Input: nums = [4,3,2,7,8,2,3,1]
#Output: [2,3]
#Example 2:

#Input: nums = [1,1,2]
#Output: [1]
#Example 3:

#Input: nums = [1]
#Output: []

#my own solution in python3:

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        d = dict()
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
        for key in d:
            if d[key] >= 2:
                res.append(key)
        return res

#9/8/24 review from grokking course:

def find_duplicates(nums):
    res = []
    for n in nums:
      if nums.count(n) > 1:
        res.append(n)
    myset = set()
    for r in res:
      myset.add(r)
    ans = []
    for s in myset:
      ans.append(s)
    return ans
