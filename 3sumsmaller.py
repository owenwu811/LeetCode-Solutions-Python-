
#259
#medium


#Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

 

#Example 1:

#Input: nums = [-2,0,1,3], target = 2
#Output: 2
#Explanation: Because there are two triplets which sums are less than 2:
#[-2,0,1]
#[-2,0,3]
#Example 2:

#Input: nums = [], target = 0
#Output: 0
#Example 3:

#Input: nums = [0], target = 0
#Output: 0



#my own solution using python3:

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()
        for first in range(len(nums) - 2):
            second = first + 1
            third = len(nums) - 1
            while second <= third:
                threesum = nums[first] + nums[second] + nums[third]
                if threesum < target:
                    res += abs(second - third)
                    second += 1
                else:
                    third -= 1
        return res
