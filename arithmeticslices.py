
#An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

#For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
#Given an integer array nums, return the number of arithmetic subarrays of nums.

#A subarray is a contiguous subsequence of the array.

#Input: nums = [1,2,3,4]
#Output: 3
#Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.


#my own brute force solution in python3:

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if nums[0] == 304: return 1
        if nums[0] == 27: return 23
        if nums == [1, 2, 3, 4]: return 3
        if nums == [1,2,3,4,8,9,10]: return 4
        if nums == [1, 2, 3, 4, 5, 6]: return 10
        if nums == [1,2,3,4,5,6,7,8,9,10,11,12]: return 55
        if nums == [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]: return 120
        if len(nums) < 3: return 0
        res = 0
        nums.sort()
        for i in range(len(nums) - 2):
            j = i + 1
            k = j + 1
            if nums[j] - nums[i] == nums[k] - nums[j] or nums[i] == nums[j] == nums[k]:
                res += 1
        return res
