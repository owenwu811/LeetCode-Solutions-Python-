
#453
#medium

#Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

#In one move, you can increment n - 1 elements of the array by 1.

#correct python3 solution:

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - len(nums) * min(nums)
        #[1,1,1000000000]
