#152. Maximum Product Subarray
#Given an integer array nums, find a 
#subarray that has the largest product, and return the product.
#The test cases are generated so that the answer will fit in a 32-bit integer.

#Example 1:

#Input: nums = [2,3,-2,4]
#Output: 6
#Explanation: [2,3] has the largest product 6.
#Example 2:

#Input: nums = [-2,0,-1]
#Output: 0
#Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 
#Constraints:

#1 <= nums.length <= 2 * 104
#-10 <= nums[i] <= 10
#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#Accepted
#1.1M
#Submissions
#3.2M
#Acceptance Rate
#34.8%

#correct anwser:

class Solution:
    import math
    def maxProduct(self, nums: List[int]) -> int:
        #this is a dynamic programming problem, not a sliding window
        #we have to keep track of the min and max of each subarray
        #for example, if [-1, -2], the max would be 2 while the min would be -2
        #and then for [-1, -2, -3], we would take -3 and multiple -3 by both the min and max of the previous -2 and 2, we would get -6 and 6, and if the array was [-1, -2, -3, -4], we would take -4 and multiple it by -6 vs 4 * 6 and compare both to get 24 as max and -24 as min and so on
        #if we run into 0, we set min and max to 1 to nuetralize the value so we start over since anything times 0 is just 0, so we ignore the 0 while keeping our historical biggest max product subarray
        res = max(nums)
        curMin, curMax = 1, 1
        for n in nums:
            if n == 0: #this is the case where we hit a 0 because if we multiply by 0, we get 0, and the rest of the future solutions will stay as 0
                curMin, curMax = 1, 1
                continue #continue to next iteration of loop
            tmp = curMax * n 
            curMax = max(n * curMax, n * curMin, n) #recomputing currmin and currmax - n * curMax is when both are positive and n * curMin is when both are negative, resulting in positive
            #n is for when [-1, 8] - the max itself would be 8
            curMin = min(n * curMin, tmp, n) #tmp is for using the old currmax
            res = max(res, curMax) 
        return res

#3/30/24 refresher (missed):


class Solution:
    import math
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmin, curmax = 1, 1
        for n in nums:
            if n == 0:
                curmin, curmax = 1, 1
                continue
            temp = curmax * n #reason for temp variable - think about [-1, 8] case
            curmax = max(n * curmax, n * curmin, n)
            curmin = min(n * curmin, temp, n)
            res = max(res, curmax, curmin)
        return res

#3/30/24 practice round two:

class Solution:
    import math
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) #[-1]
        curmin, curmax = 1, 1
        for n in nums:
            if n == 0:
                curmin, curmax = 1, 1
                continue
            temp = curmax * n #[-1, 8]
            curmax = max(n * curmax, n * curmin, n)
            curmin = min(n * curmin, temp, n)
            res = max(res, curmax)
        return res

#3/31/24:

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmin, curmax = 1, 1
        for n in nums:
            if n == 0:
                curmin, curmax = 1, 1
                continue
            temp = curmax * n
            curmax = max(n * curmax, n * curmin, n)
            curmin = min(n * curmin, temp, n)
            res = max(res, curmax, curmin)
        return res

#4/1/24:

class Solution:
    import math
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmin, curmax = 1, 1
        for n in nums:
            if n == 0:
                curmin, curmax = 1, 1
                continue
            temp = n * curmax
            curmax = max(n * curmax, n * curmin, n)
            curmin = min(n * curmin, temp, n)
            res = max(res, curmax)
        return res
        

#4/2/24 practice:

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) #[-1]
        curmin, curmax = 1, 1
        for n in nums: #n is our current number
            if n == 0:
                curmin, curmax = 1, 1
                continue
            #only when n is not equal to 0 does this execute, so since n starts at 2, 2 != 0, so this line executes
            temp = curmax * n #[-1, 8]
            curmax = max(curmax * n, curmin * n, n) #even though curmax was 6 for n == 3 iteration, since n = -2 now, curmax = max(6 * -2, 3 * -2, -2), so curmax actually decreases from 6 to -2
            curmin = min(curmin * n, temp, n) #even though curmin was 2, for the n == 3 iteration in [2, 3, -2, 4], curmin = min(2 * 3, 6, 3), so curmin actually increases from 2 to 3
            res = max(res, curmax) #for test case [2, 3, -2, 4], res = 4, and even though curmax = 2, 4 > 2, so res stays 4
        return res

#4/5/24 practice:

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmin, curmax = 1, 1
        res = max(nums) #[-1]
        for n in nums:
            if n == 0:
                curmin, curmax = 1, 1
                continue
            temp = curmax * n
            curmax = max(curmin * n, curmax * n, n)
            curmin = min(curmin * n, temp, n) #[-1, 8]
            res = max(res, curmax, curmin)
        return res

#4/9/24:

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmin, curmax = 1, 1
        for n in nums:
            if n == 0:
                curmin, curmax = 1, 1
                continue
            temp = curmax * n
            curmax = max(curmin * n, curmax * n, n) #the ordering matters too - curmax line must come first
            curmin = min(curmin * n, temp, n) #not using temp and using curmax * n would fail nums = [-4,-3,-2], giving us 72 instead of 12 as the output
            res = max(res, curmax)
        return res
