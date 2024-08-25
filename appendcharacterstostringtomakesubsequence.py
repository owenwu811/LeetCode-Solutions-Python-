#medium
#73% acceptance rate


#You are given two strings s and t consisting of only lowercase English letters.

#Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

#A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

 

#Example 1:

#Input: s = "coaching", t = "coding"
#Output: 4
#Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
#Now, t is a subsequence of s ("coachingding").
#It can be shown that appending any 3 characters to the end of s will never make t a subsequence.



#correct python3 solution (I couldn't solve it):

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        for i in range(len(s)):
            if j < len(t) and s[i] == t[j]:
                j += 1
            if j >= len(t):
                break
        return len(t) - j
