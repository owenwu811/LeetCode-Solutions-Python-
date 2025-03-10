
#553
#medium

#You are given an integer array nums. The adjacent integers in nums will perform the float division.

#For example, for nums = [2,3,4], we will evaluate the expression "2/3/4".
#However, you can add any number of parenthesis at any position to change the priority of operations. You want to add these parentheses such the value of the expression after the evaluation is maximum.

#Return the corresponding expression that has the maximum value in string format.

#Note: your expression should not contain redundant parenthesis.

 

#Example 1:

#Input: nums = [1000,100,10,2]
#Output: "1000/(100/10/2)"
#Explanation: 1000/(100/10/2) = 1000/((100/10)/2) = 200
#However, the bold parenthesis in "1000/((100/10)/2)" are redundant since they do not influence the operation priority.
#So you should return "1000/(100/10/2)".
#Other cases:
#1000/(100/10)/2 = 50
#1000/(100/(10/2)) = 50
#1000/100/10/2 = 0.5
#1000/100/(10/2) = 2


#my own solution using python3:

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])
        cur = ""
        for i, n in enumerate(nums):
            if i == 0:
                cur += str(n)
                cur += "/"
                cur += "("
            elif i == len(nums) - 1:
                cur += str(n)
                cur += ")"
            else:
                cur += str(n)
                cur += "/"
        return cur
