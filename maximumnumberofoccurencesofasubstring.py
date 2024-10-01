
#1297
#medium

#Given a string s, return the maximum number of occurrences of any substring under the following rules:

#The number of unique characters in the substring must be less than or equal to maxLetters.
#The substring size must be between minSize and maxSize inclusive.
 

#Example 1:

#Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
#Output: 2
#Explanation: Substring "aab" has 2 occurrences in the original string.
#It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).



#my TLE 33/40 solution:

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        tmp = []
        d = defaultdict(int)
        for i in range(len(s)):
            for j in range(i, len(s)):
                window = s[i: j + 1]
                if len(set(window)) <= maxLetters and minSize <= len(window) <= maxSize:
                    tmp.append(window)
                    d[window] += 1
        if d:
            return max(d.values())
        return 0


#correct python3 solution (wasn't able to solve):

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        tmp = []
        d = defaultdict(int)
        l = 0
        for i in range(len(s)):
            window = s[i: i + minSize]
            if len(set(window)) <= maxLetters and minSize <= len(window) <= maxSize:
                d[window] += 1
        print(d)
        return max(d.values()) if d else 0
        
