
#3115
#medium


#You are given an integer array nums.

#Return an integer that is the maximum distance between the indices of two (not necessarily different) prime numbers in nums.

 

#Example 1:

#Input: nums = [4,2,9,5,3]

#Output: 3

#Explanation: nums[1], nums[3], and nums[4] are prime. So the answer is |4 - 1| = 3.

#Example 2:

#Input: nums = [4,8,2,8]

#Output: 0

#Explanation: nums[2] is prime. Because there is just one prime number, the answer is |2 - 2| = 0.



#my own solution using python3 after looking up which numbers are prime from 0 to 100:

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        primed = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        tmp = []
        for i, n in enumerate(nums):
            if n in primed:
                tmp.append([i, n])
        print(tmp)
        result = []
        for t in tmp:
            result.append(t[0])
        return abs(max(result) - min(result))
