
#2221
#medium

#You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).

#The triangular sum of nums is the value of the only element present in nums after the following process terminates:

#Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n - 1.
#For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes modulo operator.
#Replace the array nums with newNums.
#Repeat the entire process starting from step 1.
#Return the triangular sum of nums.


#my own solution using python3:

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        self.ans = []
        def f(arr):
            if len(arr) == 1:
                return arr[0]
            res = []
            for i in range(1, len(arr)):
                res.append(arr[i] + arr[i - 1])
            arr = res
            self.ans.append(res)
            f(res)
        f(nums)
        n = []
        for a in self.ans:
            for i in range(len(a)):
                n.append(a[i])
        j = []
        for g in str(n[-1]):
            j.append(g)
        return int(j[-1])
