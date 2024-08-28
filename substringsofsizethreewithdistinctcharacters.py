#easy
#73.9% accpetance rate 


#A string is good if there are no repeated characters.

#Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

#Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

#A substring is a contiguous sequence of characters in a string.



#my own solution using python3:

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = 0
        myset = set()
        for i in range(0, len(s) - 2, 1):
            window = s[i: i + 3]
            if len(window) == len(set(window)):
            #print(window)
                res += 1
        return res
