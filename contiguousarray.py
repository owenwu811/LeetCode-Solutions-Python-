#Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

#nums = [0,0,1,0,0,0,1,1] > 6


#python3 solution:

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff = {}
        needhowmanyzeros, res = 0, 0
        for curindex, val in enumerate(nums):
            if val == 1:
                needhowmanyzeros += 1
            else:
                needhowmanyzeros -= 1
            if needhowmanyzeros not in diff:
                diff[needhowmanyzeros] = curindex
            if needhowmanyzeros == 0: #we don't owe any more 0s up to the current index meaning that the entire array up to the current point has an equal number of 0s and 1s, then the entire array up to the current index counts as a potential result
                res = curindex + 1 #we want length
            else:
                res = max(res, curindex - diff[needhowmanyzeros]) 
        return res

#needhowmanyzeros represents how many extra 0s we need to balance out the number of 1s we have seen so far, and curindex - diff[needhowmanyzeros] means the current index minus the allowance we still owe 

  
