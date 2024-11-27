

#3300
#easy

#You are given an integer array nums.

#You replace each element in nums with the sum of its digits.

#Return the minimum element in nums after all replacements.

 

#Example 1:

#Input: nums = [10,12,13,14]

#Output: 1

#Explanation:

#nums becomes [1, 3, 4, 5] after all replacements, with minimum element 1.


#my own solution using python3:

class Solution:
    def minElement(self, nums: List[int]) -> int:
        new = []
        for n in nums:
            print(n)
            cur = 0
            for i in str(n):
                cur += int(i)
            print(cur)
            new.append(cur)
        return min(new)
