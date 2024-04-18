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
                # 0 0 1 0 - max( res, 3 - 1) during curindex = 3, so res = 2 here as well even though res became 2 during curindex = 2 - 0 0 1
                res = max(res, curindex - diff[needhowmanyzeros]) #0 0 1 0 - at this point, needhowmanyzeros = -2 at index 3 because we still need 2 more 1s than we have in this window to balance out
        return res

#needhowmanyzeros represents how many extra 0s we need to balance out the number of 1s we have seen so far, and curindex - diff[needhowmanyzeros] means the current index minus the allowance we still owe 

  
