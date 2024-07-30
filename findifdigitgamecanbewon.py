#You are given an array of positive integers nums.

#Alice and Bob are playing a game. In the game, Alice can choose either all single-digit numbers or all double-digit numbers from nums, and the rest of the numbers are given to Bob. Alice wins if the sum of her numbers is strictly greater than the sum of Bob's numbers.

#Return true if Alice can win this game, otherwise, return false.

# Input: nums = [1,2,3,4,10]

#Output: false

#Explanation:

#Alice cannot win by choosing either single-digit or double-digit numbers.


#my very own solution in python3:

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        totsum = sum(nums)
        halfsum = totsum // 2
        singlesum, doublesum = 0, 0
        for n in nums:
            if n < 10:
                singlesum += n
            else:
                doublesum += n
        return doublesum > halfsum or singlesum > halfsum

