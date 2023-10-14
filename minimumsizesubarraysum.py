#209. Minimum Size Subarray Sum
#Medium
#11.8K
#353
#Companies
#Given an array of positive integers nums and a positive integer target, return the minimal length of a
#subarray
# whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

#Example 1:

#Input: target = 7, nums = [2,3,1,2,4,3]
#Output: 2
#Explanation: The subarray [4,3] has the minimal length under the problem constraint.
#Example 2:

#Input: target = 4, nums = [1,4,4]
#Output: 1
#Example 3:

#Input: target = 11, nums = [1,1,1,1,1,1,1,1]
#Output: 0
 

#Constraints:

#1 <= target <= 109
#1 <= nums.length <= 105
#1 <= nums[i] <= 104
 

#Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
#Accepted
#868.3K
#Submissions
#1.9M
#Acceptance Rate
#46.5%

#My Solution (Python3):

class Solution:
    import math
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if nums[0] >= target or nums[-1] >= target:
            return 1
        res = len(nums) #6, 8
        currsum, ws = 0, 0
        for we in range(len(nums)): #we = 012345, 01234567
            currsum += nums[we] #currsum = 0 + 2 = 2, 2 + 3 = 5, 5 + 1 = 6, 6 + 2 = 8, currsum = 0 + 1 = 1.. 1 + 1 = 2... 2 + 1 = 3.. 3 + 1 = 4.. 4 + 1 = 5..
            # 5 + 1 = 6.. 6 + 1 = 7.. 7 + 1 = 8
            if we == res - 1 and ws == 0 and currsum < target:
                return 0
            while currsum >= target:
                res = min(we - ws + 1, res) 
                #ws += 1 
                #return res
                currsum -= nums[ws]  #currsum = 8 - 2 = 6
                ws += 1 # 0 > 1
                #if currsum >= target:
            else:
                continue
        return res
#take the wrong test case, and go through your code line by line, writing down the output instead of guessing
        
