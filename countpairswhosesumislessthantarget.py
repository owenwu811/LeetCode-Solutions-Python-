
#easy
#2824

#Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.


#my own solution using python3:

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j and nums[i] + nums[j] < target:
                    res += 1
        return res
