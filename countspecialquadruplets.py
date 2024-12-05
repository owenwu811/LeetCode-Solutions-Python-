

#1995
#easy

#Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:

#nums[a] + nums[b] + nums[c] == nums[d], and
#a < b < c < d
 

#Example 1:

#Input: nums = [1,2,3,6]
#Output: 1
#Explanation: The only quadruplet that satisfies the requirement is (0, 1, 2, 3) because 1 + 2 + 3 == 6.




#my own solution using python3:

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    for d in range(k + 1, len(nums)):
                        if nums[i] + nums[j] + nums[k] == nums[d]:
                            res += 1
        return res
