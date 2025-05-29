

#2083
#medium

#You are given a 0-indexed string s consisting of only lowercase English letters. Return the number of substrings in s that begin and end with the same character.

#A substring is a contiguous non-empty sequence of characters within a string.

 

#Example 1:

#Input: s = "abcba"
#Output: 7
#Explanation:
#The substrings of length 1 that start and end with the same letter are: "a", "b", "c", "b", and "a".
#The substring of length 3 that starts and ends with the same letter is: "bcb".
#The substring of length 5 that starts and ends with the same letter is: "abcba".


#my own solution using python3 on 5/28/25:

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        #"abcba"
        # "a"

        #a b c b b a
        c = Counter(s)
        for i in range(len(s)):
            c[s[i]] -= 1
            ans += 1
            ans += c[s[i]]
            
        return ans



#correct python3 solution (could not solve):

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        d = defaultdict(int)
        for c in s:
            d[c] += 1
            res += d[c]
        return res
