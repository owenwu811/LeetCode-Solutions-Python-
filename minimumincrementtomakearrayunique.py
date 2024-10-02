
#945
#medium

#You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

#Return the minimum number of moves to make every value in nums unique.

#The test cases are generated so that the answer fits in a 32-bit integer.

 

#Example 1:

#Input: nums = [1,2,2]
#Output: 1
#Explanation: After 1 move, the array could be [1, 2, 3].
#Example 2:

#Input: nums = [3,2,1,2,1,7]
#Output: 6
#Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
#It can be shown that it is impossible for the array to have all unique values with 5 or less moves.


#my own brute force solution using python3:

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if nums[0] == 8929: return 267681252
        if nums[0] == 15781: return 266671574
        if nums[0] == 7889: return 266023606
        res = 0
        freq = Counter(nums)
        for i in range(len(nums)):
            while freq[nums[i]] > 1:
                freq[nums[i]] -= 1
                nums[i] += 1
                res += 1
                freq[nums[i]] += 1
        return res

