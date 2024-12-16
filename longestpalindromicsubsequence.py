#516
#medium

#Given a string s, find the longest palindromic subsequence's length in s.

#A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

#Example 1:

#Input: s = "bbbab"
#Output: 4
#Explanation: One possible longest palindromic subsequence is "bbbb".
#Example 2:

#Input: s = "cbbd"
#Output: 2
#Explanation: One possible longest palindromic subsequence is "bb".

#my own solution using python3:

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        m, n = len(s), len(s)
        dp = []
        for i in range(m + 1):
            cur = []
            for j in range(n + 1):
                cur.append(0)
            dp.append(cur)
        orig, flipped = s, s[::-1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if orig[i - 1] == flipped[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
