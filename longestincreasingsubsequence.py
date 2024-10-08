
#Given an integer array nums, return the length of the longest strictly increasing 
#subsequence

#Input: nums = [10,9,2,5,3,7,101,18]
#Output: 4
#Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

#python3 solution:

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1] * len(nums) #1 because we can just choose itself as longest atleast 1
        for i in range(len(nums) -1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]: #j is in front of i always since we want longest increasing sequence
                    res[i] = max(res[i], 1 + res[j])
        return max(res)


#review again:

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1] * len(nums)
        for i in range(len(nums) -1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    res[i] = max(res[i], 1 + res[j]) #[0, 1, 0, 3, 2, 3] - at index 4, when i = 4 and j = 5, 2 < 4, so res[4] (res[i] not res[j]) becomes 2. similarly, when i = 2 and j = 3, 0 < 3, so res[2] (res[i]) becomes 2
        return max(res)

#

#let's say you have [1, 3, 2, 4] - when i = 1 and j = 2, giving us 3 and 2 for i and j as values, 3 is not less than 2, so j moves forward, so do max(res[i], 1 + res[j]) because res[j] = 1 since from the last element, we only have one longest increasing length, but then the current i counts because index 1 is less than index 3, so add 1! this logic works for nums = [10,9,2,5,3,7,101,18] as well when 5 > 3, but 2 < 3, so we do 1 + res[3], and res[3] was already computed previously!


#4/24/24 refresher:

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1] * len(nums)
        for i in range(len(nums) -1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    res[i] = max(res[i], 1 + res[j])
        return max(res)

#4/26/24 refresher:

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1] * len(nums)
        for i in range(len(nums) -1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    res[i] = max(res[i], 1 + res[j])
        return max(res)


#4/27/24:

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1] * len(nums)
        for i in range(len(nums) -1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    res[i] = max(res[i], 1 + res[j])
        return max(res)


#4/28/24 refresher:

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1] * len(nums)
        for i in range(len(nums) -1, -1, -1):
            for j in range(i + 1, len(nums)): 
                if nums[i] < nums[j]:
                    res[i] = max(res[i], 1 + res[j])
        return max(res)

#5/11/24 refresher (my own solution):

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #[10, 9, 2, 5, 3, 7, 101, 18]
        res = [1] * len(nums) #[1, 1, 1, 1, 1, 1, 1, 1]
        for i in range(len(nums) -1, -1, -1): #7
            for j in range(i - 1, -1, -1): #6
                if nums[j] < nums[i]:
                    res[j] = max(res[j], 1 + res[i])
        return max(res)

#5/19/24 practice:

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1] * len(nums)
        for i in range(len(nums) -1, -1, -1):
            for j in range(i, -1, -1):
                if nums[j] < nums[i]:
                    res[j] = max(res[j], 1 + res[i])
        return max(res)

#6/21/24 review:

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    res[i] = max(res[i], 1 + res[j])
        return max(res)

#7/2/24 review:

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1] * len(nums)
        for i in range(len(nums) -2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    res[i] = max(res[i], 1 + res[j])
        return max(res)


#7/11/24 review:

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1): #we need to use -2 because j is in front of i and we don't want to go out of bounds
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    res[i] = max(res[i], res[j] + 1) #+ 1 is counting the current number as 1 length
        return max(res)
        

#9/16/24 refresher:

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #[2, 3, 5, 7]
        dp = [1] * len(nums)
        for i in range(len(nums) -1, -1, -1):
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    dp[j] = max(dp[j], dp[i] + 1)
        return max(dp)
