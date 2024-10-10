
#2535
#easy

#You are given a positive integer array nums.

#The element sum is the sum of all the elements in nums.
#The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
#Return the absolute difference between the element sum and digit sum of nums.

#Note that the absolute difference between two integers x and y is defined as |x - y|.

 

#Example 1:

#Input: nums = [1,15,6,3]
#Output: 9
#Explanation: 
#The element sum of nums is 1 + 15 + 6 + 3 = 25.
#The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
#The absolute difference between the element sum and digit sum is |25 - 16| = 9.



#my own solution using python3:

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        tot = sum(nums)
        arr = []
        for i, n in enumerate(nums):
            nums[i] = str(n)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                arr.append(nums[i][j])
        print(arr)
        digitsum = 0
        for a in arr:
            digitsum += int(a)
        return tot - digitsum
