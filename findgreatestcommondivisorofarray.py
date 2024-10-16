

#1979
#easy

#Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

#The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
 

#Example 1:

#Input: nums = [2,5,6,9,10]
#Output: 2
#Explanation:
#The smallest number in nums is 2.
#The largest number in nums is 10.
#The greatest common divisor of 2 and 10 is 2.


#my own solution using python3:

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small, large = min(nums), max(nums)
        return math.gcd(small, large)
