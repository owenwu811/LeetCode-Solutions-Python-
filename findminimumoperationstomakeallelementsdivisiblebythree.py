
#You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.

#Return the minimum number of operations to make all elements of nums divisible by 3.

#3190

#easy


#correct python3 solution:

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for number in nums:
            if number % 3 != 0:
                res += 1
        return res
