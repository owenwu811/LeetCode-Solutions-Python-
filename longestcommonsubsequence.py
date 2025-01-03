#1143
#medium

#Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

#A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

#For example, "ace" is a subsequence of "abcde".
#A common subsequence of two strings is a subsequence that is common to both strings.


#correct python3 soution (could not solve):

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = []
        for i in range(m + 1):
            cur = []
            for j in range(n + 1):
                cur.append(0)
            dp.append(cur)
        print(dp)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


#12/21/24 review:

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = []
        m, n = len(text1), len(text2)
        for i in range(m + 1):
            cur = []
            for j in range(n + 1):
                cur.append(0)
            dp.append(cur)
        print(dp)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
