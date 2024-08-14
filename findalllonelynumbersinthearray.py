#You are given an integer array nums. A number x is lonely when it appears only once, and no adjacent numbers (i.e. x + 1 and x - 1) appear in the array.

#Return all lonely numbers in nums. You may return the answer in any order.

 

#Example 1:

#Input: nums = [10,6,5,8]
#Output: [10,8]
#Explanation: 
#- 10 is a lonely number since it appears exactly once and 9 and 11 does not appear in nums.
#- 8 is a lonely number since it appears exactly once and 7 and 9 does not appear in nums.
#- 5 is not a lonely number since 6 appears in nums and vice versa.
#Hence, the lonely numbers in nums are [10, 8].
#Note that [8, 10] may also be returned.

#my own solution using python3:

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        mydict = dict()
        for n in nums:
            if n not in mydict:
                mydict[n] = 0
            mydict[n] += 1
        print(mydict)
        nums.sort()
        res = []
        for i in range(len(nums)):
            if mydict[nums[i]] == 1 and (nums[i] + 1) not in mydict and (nums[i] - 1) not in mydict:
                res.append(nums[i])

        return res
