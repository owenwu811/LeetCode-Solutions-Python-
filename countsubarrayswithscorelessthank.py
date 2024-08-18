
#Hard
#2302

#The score of an array is defined as the product of its sum and its length.

#For example, the score of [1, 2, 3, 4, 5] is (1 + 2 + 3 + 4 + 5) * 5 = 75.
#Given a positive integer array nums and an integer k, return the number of non-empty subarrays of nums whose score is strictly less than k.

#A subarray is a contiguous sequence of elements within an array.

#python3 solution:


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        cursum = 0
        l = 0
        for r in range(len(nums)):
            cursum += nums[r]
            while cursum * (r - l + 1) >= k:
                cursum -= nums[l]
                l += 1
            res += (r - l + 1)

        return res
