
#462
#medium

#Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

#In one move, you can increment or decrement an element of the array by 1.

#Test cases are designed so that the answer will fit in a 32-bit integer.


#my own solution using python3:

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        res = 0
        for n in nums:
            res += abs(median - n)
        return res
