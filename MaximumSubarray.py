#Given an integer array nums, find the 
#subarray with the largest sum, and return its sum.

#Example 1:

#Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
#Explanation: The subarray [4,-1,2,1] has the largest sum 6.
#Example 2:

#Input: nums = [1]
#Output: 1
#Explanation: The subarray [1] has the largest sum 1.
#Example 3:

#Input: nums = [5,4,-1,7,8]
#Output: 23
#Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

#Constraints:

#1 <= nums.length <= 105
#-104 <= nums[i] <= 104


#dumb way (will get TLE):

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = min(nums)
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarr = nums[i: j + 1]
                res = max(res, sum(subarr))
        return res

#My Solution:

class Solution:
    import math
    def maxSubArray(self, nums: List[int]) -> int:
        left, right, currsum, maxsum = 0, 0, 0, nums[0] #using the sliding window approach
        for right in range(len(nums)):
            currsum += nums[right]
            if currsum < 0:
                maxsum = max(maxsum, currsum)
                currsum = 0 #we are trying to nuetralize the currsum. We get rid of deadweight because negatives never contribute anything. a negative plus negative is even smaller, so you might as well just take the bigger of the two negatives. 
                right += 1
                left = right
            else:
                maxsum = max(maxsum, currsum)
        return maxsum
  #line 33 should be nums[0] and not 0 because the array may only contain negative values. 
  #line 38 is necessary


#You could also do it like this: 

class Solution:
    import math
    def maxSubArray(self, nums: List[int]) -> int:
        #largest sum means the largest out of whatever is available in the given list. if the list only has [-2], then -2 is the maximum subarray, not 0. 
        if len(nums) == 1:
            return nums[0]
        maxsum = nums[0]
        currentsum = 0 #currentsum starts at 0
        for i in range(len(nums)):
            if currentsum < 0:
                currentsum = 0 #negatives don't contribute anything, so start with a fresh slate
            currentsum += nums[i]
            maxsum = max(maxsum, currentsum)
        return maxsum


6/20/23 refresher (my solution):

class Solution:
    import math
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        currentsum = 0
        for i in nums:
            if currentsum < 0:
                currentsum = 0
            currentsum += i
            maxsum = max(maxsum, currentsum)
        return maxsum

7/1/23 refresher (my solution):

class Solution(object):
    import math
    def maxSubArray(self, nums):
        #has to include atleast one of the elemnts in the array. if there is only one negative element in the array, the result cannot be 0
        maxsum = nums[0]
        currentsum = 0
        for val in nums: #YOU MUST REMEMBER TO LOOP THROUGH NUMS TO GET THE NEXT VALUE IN THE ARRAY 
            if currentsum < 0:
                currentsum = 0
            currentsum += val #YOU ADD CURRENTSUM TO VAL TO SEE IF IT IS BIGGER AFTER NUETRALIZING IT TO 0
            maxsum = max(maxsum, currentsum) #WE COMPARE THE HISTORICAL BIGGEST MAXSUM TO WHAT YOU GET RIGHT ABOVE AFTER ADDING THE NEXT ELEMENT AFTER NUETRALIZING IT TO 0. MAXSUM WOULD ONLY BE THE BIGGEST ON THE 1ST TURN BECAUSE MAXSUM IS ONLY A STARTING POINT.
        return maxsum

#12/25/23 refresher (my solution) - kadane's algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #has to atleast be something
        result = nums[-1] # can't be nums[-2] because the input is garunteed to have atleast 1 element in it, so [] wouldn't be an input, so [-1] means that nums[-1] works at worst case but nums[-2] is out of bounds
        windowsum = 0
        for number in nums:
            if windowsum < 0:
                windowsum = 0
            windowsum += number
            result = max(result, windowsum)
        return result


#12/25/23 refresher 2 - my solution in python3:

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #we are garunteed to have atleast one element in the list as input, so nums[-2] dosen't work, but nums[-1] is always garunteed to be NOT out of bounds since we will always have atleast one element in the input
        result = nums[-1]
        windowsum = 0
        for number in nums:
            if windowsum < 0:
                windowsum = 0
            windowsum = windowsum + number
            result = max(result, windowsum)
        return result


#12/29/23 refresher - my python3 solution:

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #we want the subarray with the largest sum, not longest in any way, so this is not a sliding window - if the array only has one element, which it is gaurunteed to through the input, the only element will be the result, so start with one element instead of 0. we can't just skip negatives because the subarray wouldn't be contiguous, and a subarray, by definition, must be contiguous 
        res = nums[0]
        windowsum = 0
        for number in nums:
            if windowsum < 0:
                windowsum = 0
            windowsum += number
            res = max(res, windowsum)
        return res


#2/7/24:

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #we want a contiguous subarray inside of the nums array that, when you add all the numbers in this subarray up, the sum is larger than all other possible subarrays
        result = nums[0]
        windowsum = 0
        for number in nums:
            if windowsum < 0:
                windowsum = 0
            windowsum += number
            result = max(result, windowsum)
        return result

#3/7/24:

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #we want a contiguous subarray that has the largest sum
        res = nums[0]
        windowsum = 0
        for number in nums:
            if windowsum < 0:
                windowsum = 0
            windowsum += number
            res = max(res, windowsum)
        return res

#3/18/24:

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        windowsum = 0
        for number in nums:
            if windowsum < 0:
                windowsum = 0
            windowsum += number
            res = max(res, windowsum)
        return res

#4/3/24:

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #we want to find a contiguous subarray, which, when added together, has the largest sum of any contiguous subarrays, and we return that sum
        res = nums[0] #use nums[0] here because, with nums[-1], if array only contains negative elements, and the last element isn't the smallest. remember that algorithm loops from left to right!
        cur = 0
        for number in nums:
            if cur < 0: #asks should we continue the current subarray - if cur is indeed less than 0, then start a new subarray by nuetralizing the new subarray to 0. we are interested in finding the LARGEST SUBARRAY, NOT THE LARGEST VALUE OF i!
                cur = 0 #if we have [-2, 1], then -2 + 1 is still smaller than 1, so we can start a new subarray at 1 by first setting cur to 0 before adding i (i is 1 here)
            cur += number
            res = max(res, cur) #[-2, 1, -3]. (1 + -3) = -2, so cur = -2, but maxsum was still 1 historically, so max(1, -2) still yields 1, and after we return to line 7, cur will be reset to 0. maxsum will never be different than 1 here unless cursum happens to be bigger than 1!
        return res

#4/19/24:

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        subarraysum = 0
        for n in nums:
            if subarraysum < 0:
                subarraysum = 0
            subarraysum += n
            res = max(res, subarraysum)
        return res

#5/14/24 refresher (my own solution):

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        subarraysum = 0
        for i in nums: #[-1]
            subarraysum += i #-1
            if subarraysum < 0:
                subarraysum = 0 #0
            else:
                res = max(res, subarraysum) #max(-1, 0)
        return res

#6/8/24 review:

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        cursum = 0
        for number in nums:
            if cursum < 0:
                cursum = 0
            cursum += number
            res = max(res, cursum)
        return res

#7/15/24 refresher:

#classic kadane's algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0] 
        subarraysum = 0
        for n in nums:
            if subarraysum < 0: #each turn, we check negatives because negatives contribute nothing to a positive subarraysum
                subarraysum = 0 #nuetralize a subarray sum that we know won't be the maximum 
            subarraysum += n
            res = max(res, subarraysum)
        return res

#8/9/24 review:

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        cursum = 0
        for n in nums: #if we put cursum += n right below the for loop, we will fail test case [-1], outputing 0 instead of -1
            if cursum < 0:
                cursum = 0
            cursum += n
            res = max(res, cursum)
        return res

#10/13/24 review:

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        subarraysum = 0
        for n in nums:
            if subarraysum < 0:
                subarraysum = 0
            subarraysum += n
            res = max(res, subarraysum)
        return res

#12/16/24 review:

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = min(nums)
        subarr = 0
        for n in nums:
            if subarr < 0:
                subarr = 0
            subarr += n
            res = max(res, subarr)
        return res
