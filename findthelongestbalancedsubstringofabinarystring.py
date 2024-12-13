

#2609
#easy

#You are given a binary string s consisting only of zeroes and ones.

#A substring of s is considered balanced if all zeroes are before ones and the number of zeroes is equal to the number of ones inside the substring. Notice that the empty substring is considered a balanced substring.

#Return the length of the longest balanced substring of s.

#A substring is a contiguous sequence of characters within a string.

 

#Example 1:

#Input: s = "01000111"
#Output: 6
#Explanation: The longest balanced substring is "000111", which has length 6.



#my own solution using python3:

class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                substr = s[i: j + 1]
                if substr.count("0") == substr.count("1") and substr == "".join(sorted(substr)):
                    res = max(res, len(substr))
        return res
