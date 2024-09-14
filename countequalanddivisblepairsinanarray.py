
#2176

#Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.

#my own solution using python3:

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if 0 <= i < j < len(nums) and nums[i] == nums[j] and (i * j) % k == 0:
                    res += 1
        return res
