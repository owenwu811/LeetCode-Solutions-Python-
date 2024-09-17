
#646
#medium

#You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

#A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

#Return the length longest chain which can be formed.

#You do not need to use up all the given intervals. You can select pairs in any order.


#my own solution using python3 after reading clues from discussion section about sorting and how similar to Longest increasing subsequence problem:

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        dp = [1] * len(pairs)
        for i in range(len(pairs) -1, -1, -1):
            for j in range(i - 1, -1, -1):
                if pairs[j][1] < pairs[i][0]:
                    dp[j] = max(dp[j], dp[i] + 1)
        return max(dp)
