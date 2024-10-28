#1085
#easy


#Given an integer array nums, return 0 if the sum of the digits of the minimum integer in nums is odd, or 1 otherwise.

 

#Example 1:

#Input: nums = [34,23,1,24,75,33,54,8]
#Output: 0
#Explanation: The minimal element is 1, and the sum of those digits is 1 which is odd, so the answer is 0.
#Example 2:

#Input: nums = [99,77,33,66,55]
#Output: 1
#Explanation: The minimal element is 33, and the sum of those digits is 3 + 3 = 6 which is even, so the answer is 1.



#my own solution using python3:

class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        target = min(nums)
        print(target)
        res = 0
        for i in str(target):
            res += int(i)
        print(res)
        if res % 2 != 0:
            return 0
        else:
            return 1
