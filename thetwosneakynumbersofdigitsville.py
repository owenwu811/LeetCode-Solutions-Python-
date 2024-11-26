
#3289
#easy

#In the town of Digitville, there was a list of numbers called nums containing integers from 0 to n - 1. Each number was supposed to appear exactly once in the list, however, two mischievous numbers sneaked in an additional time, making the list longer than usual.

#As the town detective, your task is to find these two sneaky numbers. Return an array of size two containing the two numbers (in any order), so peace can return to Digitville.

 

#Example 1:

#Input: nums = [0,1,1,0]

#Output: [0,1]

#Explanation:

#The numbers 0 and 1 each appear twice in the array.


#my own solution using python3:

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            if nums.count(n) > 1:
                if n not in res:
                    res.append(n)
        return res
