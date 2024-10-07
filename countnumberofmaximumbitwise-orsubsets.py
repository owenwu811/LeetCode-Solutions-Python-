
#2044
#medium

#Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.

#An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.

#The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).

 

#Example 1:

#Input: nums = [3,1]
#Output: 2
#Explanation: The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
#- [3]
#- [3,1]
#Example 2:

#Input: nums = [2,2,2]
#Output: 7
#Explanation: All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 23 - 1 = 7 total subsets.



#my own solution using python3:

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.res = []
        def f(i, nums, stack):
            if i >= len(nums):
                self.res.append(stack.copy())
                return
            stack.append(nums[i])
            f(i + 1, nums, stack)
            stack.pop()
            f(i + 1, nums, stack)
        f(0, nums, [])
        result = nums[0]
        maxn = 0
        for i in range(len(nums)):
            result = result | nums[i]
            maxn = max(maxn, result)
        res = 0
        for r in self.res:
            if len(r) == 1:
                if r[0] == maxn:
                    res += 1
                    continue
            if not r:
                continue
            owen = r[0]
            for i in range(len(r)):
                owen = owen | r[i]
            if owen == maxn:
                res += 1
        return res
