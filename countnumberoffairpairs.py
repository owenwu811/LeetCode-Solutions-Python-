
#2563
#medium

#Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

#A pair (i, j) is fair if:

#0 <= i < j < n, and
#lower <= nums[i] + nums[j] <= upper
 

#Example 1:

#Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
#Output: 6
#Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
#Example 2:

#Input: nums = [1,7,9,2,5], lower = 11, upper = 11
#Output: 1
#Explanation: There is a single fair pair: (2,3).


#my own brute force solution passing 47/54 test cases:



class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                curs = nums[i] + nums[j]
                if lower <= curs <= upper:
                    res += 1
        return res
        


#correct python3 solution:


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        while l < r:
            cursum = nums[l] + nums[r]
            if cursum > upper:
                r -= 1
            else:
                res += (r - l)
                l += 1
        l, r = 0, len(nums) - 1
        while l < r:
            cursum = nums[l] + nums[r]
            if cursum > lower - 1:
                r -= 1
            else:
                res -= (r - l)
                l += 1
        return res

                
