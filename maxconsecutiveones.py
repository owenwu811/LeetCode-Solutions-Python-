
#easy
#60.3% acceptance rate
#485

#Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

#Example 1:

#Input: nums = [1,1,0,1,1,1]
#Output: 3
#Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
#Example 2:

#Input: nums = [1,0,1,1,0,1]
#Output: 2

#my own solution using python3:

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        res = 0
        record = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                record += 1
                res = max(res, record)
            elif nums[r] == 0:
                record = 0
            
        return res


#my own solution review using python3 on 6/5/25:

#keep track of all index locations of 1s and build a dp array to find the longest consecutive sequence

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for i, n in enumerate(nums):
            d[n].append(i)
        target = d[1]
        if 1 not in nums:
            return 0
        print(target)
        dp = [1] * len(target)
        #[1, 2, 1, 2, 3]
        #[1, 1, 2, 1]
        for i in range(1, len(target)):
            if target[i] == target[i - 1] + 1:
                dp[i] = dp[i - 1] + 1
        print(dp)
        return max(dp)
