#A message containing letters from A-Z can be encoded into numbers using the following mapping:

#'A' -> "1"
#'B' -> "2"
#...
#'Z' -> "26"
#To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

#"AAJF" with the grouping (1 1 10 6)
#"KJF" with the grouping (11 10 6)
#Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

#Given a string s containing only digits, return the number of ways to decode it.

#The test cases are generated so that the answer fits in a 32-bit integer.

#Example 1:

#Input: s = "12"
#Output: 2
#Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
#Example 2:

#Input: s = "226"
#Output: 3
#Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
#Example 3:

#Input: s = "06"
#Output: 0
#Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

#python3 solution:

class Solution:
    def numDecodings(self, s: str) -> int:
        # Edge case: empty string or starts with '0' cannot be decoded
        if not s or s[0] == '0': return 0
        inputlen = len(s)
        dp = [0] * (inputlen + 1)
        # Base cases
        dp[0] = 1  # There's one way to decode an empty string
        dp[1] = 1  # There's one way to decode a non-'0' single character string
        # we start at 2 because base cases for 0 and 1 have already been handled, and we process string starting from 2nd character onwards
        for i in range(2, inputlen + 1):
            # Single digit check
            single_digit = int(s[i-1:i])  # s[i-1] is the current character
            if 1 <= single_digit <= 9:
                dp[i] += dp[i-1]
            
            # Double digit check
            double_digit = int(s[i-2:i])  # s[i-2:i] is the last two characters
            if 10 <= double_digit <= 26:
                dp[i] += dp[i-2]

        # The result is the number of ways to decode the entire string
        return dp[inputlen]

        #s = "12" > 1 and 2 count as ONE way NOT TWO WAYS to decode while 12 counts as another way
