

#974
#medium

#Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

#A subarray is a contiguous part of an array.

 

#Example 1:

#Input: nums = [4,5,0,-2,-3,1], k = 5
#Output: 7
#Explanation: There are 7 subarrays with a sum divisible by k = 5:
#[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
#Example 2:

#Input: nums = [5], k = 9
#Output: 0


#correct python3 solution: (could not solve by myself):

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        res = 0
        subarraysum = 0
        for n in nums:
            subarraysum += n
            if (subarraysum % k) in d:
                res += d[subarraysum % k]
            else:
                d[subarraysum % k] = 0
            d[subarraysum % k] += 1
        return res


#9/23/24 review:

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        res = 0
        subarraysum = 0
        for n in nums:
            subarraysum += n
            if (subarraysum % k) in d:
                res += d[subarraysum % k]
            else:
                d[subarraysum % k] = 0
            d[subarraysum % k] += 1
        return res
            

#9/25/24 review (was able to resolve):

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        subarraysum = 0
        res = 0
        for n in nums:
            subarraysum += n
            if (subarraysum % k) in d:
                res += d[subarraysum % k]
            elif (subarraysum % k) not in d:
                d[subarraysum % k] = 0
            d[subarraysum % k] += 1
        return res


#my own solution using python3 on 2/10/25:

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        cur = 0
        res = 0
        for i, n in enumerate(nums):
            cur += n
            res += d[cur % k]
            d[cur % k] += 1
        return res
