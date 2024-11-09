

#3151
#easy


#An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

#You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

 
#Example 1:

#Input: nums = [1]

#Output: true

#Explanation:

#There is only one element. So the answer is true.



#my own solution using python3:

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i] % 2 == 0 and nums[i - 1] % 2 == 0 or nums[i] % 2 != 0 and nums[i - 1] % 2 != 0:
                return False
        return True
