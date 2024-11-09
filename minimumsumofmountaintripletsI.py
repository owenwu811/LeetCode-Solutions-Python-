
#2908
#easy

#You are given a 0-indexed array nums of integers.

#A triplet of indices (i, j, k) is a mountain if:

#i < j < k
#nums[i] < nums[j] and nums[k] < nums[j]
#Return the minimum possible sum of a mountain triplet of nums. If no such triplet exists, return -1.

 

#Example 1:

#Input: nums = [8,6,1,5,3]
#Output: 9
#Explanation: Triplet (2, 3, 4) is a mountain triplet of sum 9 since: 
#- 2 < 3 < 4
#- nums[2] < nums[3] and nums[4] < nums[3]
#And the sum of this triplet is nums[2] + nums[3] + nums[4] = 9. It can be shown that there are no mountain triplets with a sum of less than 9.


#my own solution using python3:

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        res = float('inf')
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] < nums[j] > nums[k]:
                        res = min(res, nums[i] + nums[j] + nums[k])
        if res != float('inf'):
            return res
        return -1
