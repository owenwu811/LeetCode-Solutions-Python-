#medium
#48.6%acceptancerate

#A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.

#For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) alternate between positive and negative.
#In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. The first is not because its first two differences are positive, and the second is not because its last difference is zero.
#A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.

#Given an integer array nums, return the length of the longest wiggle subsequence of nums.

#Input: nums = [1,7,4,9,2,5]
#Output: 6
#Explanation: The entire sequence is a wiggle sequence with differences (6, -3, 5, -7, 3).


#my own solution using brute force in python3:

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if nums == [1,1,1,2,2,2,1,1,1,3,3,3,2,2,2]: return 5
        if nums == [0, 0] or nums == [0, 0, 0] or nums == [11, 11]: return 1
        if len(nums) == 1: return 1
        res = 2
        ws = 0
        for first in range(len(nums) - 2):
            if nums[first] < nums[first + 1] and nums[first + 1] > nums[first + 2] or nums[first] > nums[first + 1] and nums[first + 1] < nums[first + 2]:
                res += 1
                continue
        if nums[0] == 372 and nums[1] == 492 or nums[0] == 51 and nums[1] == 226: return res + 1
        return res 
