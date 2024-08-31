
#medium
#2023

#Given an array of digit strings nums and a digit string target, return the number of pairs of indices (i, j) (where i != j) such that the concatenation of nums[i] + nums[j] equals target.


#correct python3 solution:

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:  
        res = 0
        for i in range(len(nums)):
            for j in range(len(nums)): #not for j in range(i, len(nums)):!
                if i != j: 
                    if nums[i] + nums[j] == target:
                        res += 1
        return res
