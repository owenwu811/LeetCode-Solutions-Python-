
#2219
#medium

#You are given a 0-indexed integer array nums of length n.

#The sum score of nums at an index i where 0 <= i < n is the maximum of:

#The sum of the first i + 1 elements of nums.
#The sum of the last n - i elements of nums.
#Return the maximum sum score of nums at any index.

 

#Example 1:

#Input: nums = [4,3,-2,5]
#Output: 10
#Explanation:
#The sum score at index 0 is max(4, 4 + 3 + -2 + 5) = max(4, 10) = 10.
#The sum score at index 1 is max(4 + 3, 3 + -2 + 5) = max(7, 6) = 7.
#The sum score at index 2 is max(4 + 3 + -2, -2 + 5) = max(5, 3) = 5.
#The sum score at index 3 is max(4 + 3 + -2 + 5, 5) = max(10, 5) = 10.
#The maximum sum score of nums is 10.

#my own solution using python3:

class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        prefixarr = list(itertools.accumulate(nums))
        print(prefixarr)
        cur = 0
        res = []
        for i, n in enumerate(nums):
            if i == 0:
                first = prefixarr[i]
                second = sum(nums)
            else:
                first = prefixarr[i]
                second = prefixarr[-1] - prefixarr[i - 1]
            if first > second:
                res.append(first)
            else:
                res.append(second)
        return max(res)
