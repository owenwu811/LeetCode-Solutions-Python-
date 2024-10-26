
#3173
#easy


#Given an array nums of length n, return an array answer of length n - 1 such that answer[i] = nums[i] | nums[i + 1] where | is the bitwise OR operation.

 

#Example 1:

#Input: nums = [1,3,7,15]

#Output: [3,7,15]

#Example 2:

#Input: nums = [8,4,2]

#Output: [12,6]

#Example 3:

#Input: nums = [5,4,9,11]

#Output: [5,13,11]


#my own solution using python3:

class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(1, len(nums)):
            res.append(nums[i] | nums[i - 1])
        print(res)
        return res
