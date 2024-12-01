

#3309
#medium

#You are given an array of integers nums of size 3.

#Return the maximum possible number whose binary representation can be formed by concatenating the binary representation of all elements in nums in some order.

#Note that the binary representation of any number does not contain leading zeros.

 

#Example 1:

#Input: nums = [1,2,3]

#Output: 30

#Explanation:

#Concatenate the numbers in the order [3, 1, 2] to get the result "11110", which is the binary representation of 30.


#my own solution using python3:

class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        #print(bin(16)[2:])
        #print(bin(8)[2:])
        #print(bin(2)[2:])
        res = 0
        for a in permutations(nums):
            new = ""
            for j in a:
                new += str(bin(j)[2:])
            print(new)
            print(int(new, 2))
            res = max(res, int(new, 2))
        return res
