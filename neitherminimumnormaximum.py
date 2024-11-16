
#2733
#easy

#Given an integer array nums containing distinct positive integers, find and return any number from the array that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.

#Return the selected integer.

 

#Example 1:

#Input: nums = [3,2,1,4]
#Output: 2
#Explanation: In this example, the minimum value is 1 and the maximum value is 4. Therefore, either 2 or 3 can be valid answers.


#my own solution using python3:

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1 
        smallest, largest = min(nums), max(nums)
        for n in nums:
            if n != smallest and n != largest:
                return n
