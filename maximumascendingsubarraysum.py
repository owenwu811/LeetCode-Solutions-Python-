


#1800
#easy

#Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

#A subarray is defined as a contiguous sequence of numbers in an array.

#A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.

 

#Example 1:

#Input: nums = [10,20,30,5,10,50]
#Output: 65
#Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.

#my own solution using python3:

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            cur = []
            cur.append(nums[i])
            for j in range(i + 1, len(nums)):
                #print(nums[i], nums[j])
                if nums[j] > cur[-1]:
                    cur.append(nums[j])
                else:
                    break
                print(cur)
                res = max(res, sum(cur))
        if res == 0:
            return max(nums)
        return max(res, max(nums))
                
                    
