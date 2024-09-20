


#775

#medium

You are given an integer array nums of length n which represents a permutation of all the integers in the range [0, n - 1].

The number of global inversions is the number of the different pairs (i, j) where:

0 <= i < j < n
nums[i] > nums[j]
The number of local inversions is the number of indices i where:

0 <= i < n - 1
nums[i] > nums[i + 1]
Return true if the number of global inversions is equal to the number of local inversions.




#my solution that got TLE 159/226:

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        g, l = 0, 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    g += 1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                l += 1
        return g == l
            




#correct python3 solution:

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        for i, n in enumerate(nums):
            if abs(n - i) > 1: #idea is that because local inversions are counted one at a time up to that point, if global is anything more, then return False
                return False
        return True
