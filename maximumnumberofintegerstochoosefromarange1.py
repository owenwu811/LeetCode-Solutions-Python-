

#medium
#54.3% acceptance rate

#You are given an integer array banned and two integers n and maxSum. You are choosing some number of integers following the below rules:

#The chosen integers have to be in the range [1, n].
#Each integer can be chosen at most once.
#The chosen integers should not be in the array banned.
#The sum of the chosen integers should not exceed maxSum.
#Return the maximum number of integers you can choose following the mentioned rules.

#Input: banned = [1,6,5], n = 5, maxSum = 6
#Output: 2
#Explanation: You can choose the integers 2 and 4.
#2 and 4 are from the range [1, 5], both did not appear in banned, and their sum is 6, which did not exceed maxSum.

#my own solution using python3:

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        myset = set()
        for b in banned:
            myset.add(b)
        prefixsum = 0
        res = []
        for i in range(1, n + 1):
            prefixsum += i
            if i in myset or prefixsum > maxSum:
                prefixsum -= i
                continue
            else:
                res.append(i)
        return len(res)
