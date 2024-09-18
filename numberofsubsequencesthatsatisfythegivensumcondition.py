

#1498
#medium


#You are given an array of integers nums and an integer target.

#Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.

 

#Example 1:

#Input: nums = [3,5,6,7], target = 9
#Output: 4
#Explanation: There are 4 subsequences that satisfy the condition.
#[3] -> Min value + max value <= target (3 + 3 <= 9)
#[3,5] -> (3 + 5 <= 9)
#[3,5,6] -> (3 + 6 <= 9)
#[3,6] -> (3 + 6 <= 9)


#my own solution using python3 after borrowing a tiny part from another solution:

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        while l <= r:
            cursum = nums[l] + nums[r]
            if cursum > target:
                r -= 1
            elif cursum <= target:
                res += (2 ** (r - l)) #the number of subsequences if 2 ** (r - l)!!!!
                l += 1
        return res % ((10 ** 9) + 7)
 
