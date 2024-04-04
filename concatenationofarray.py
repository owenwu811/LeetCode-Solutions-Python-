


#Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

#Specifically, ans is the concatenation of two nums arrays.

#Return the array ans.

#Input: nums = [1,2,1]
#Output: [1,2,1,1,2,1]


#my solution in python3:

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        list1 = nums
        list2 = nums
        return list1 + list2
