
#3364
#easy

#contest question # 1 on November 23, 2024

#You are given an integer array nums and two integers l and r. Your task is to find the minimum sum of a subarray whose size is between l and r (inclusive) and whose sum is greater than 0.

#Return the minimum sum of such a subarray. If no such subarray exists, return -1.

#A subarray is a contiguous non-empty sequence of elements within an array.

#Input: nums = [3, -2, 1, 4], l = 2, r = 3

#Output: 1


#my own solution using python3:

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        small, large = l, r
        print(small, large)
        res = float('inf')
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarr = nums[i: j + 1]
                if l <= len(subarr) <= r:
                    if sum(subarr) > 0:
                        res = min(res, sum(subarr))
        if res == float('inf'):
            return -1
        return res
        
        
