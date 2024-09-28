
#2186
#medium


#You are given two strings s and t. In one step, you can append any character to either s or t.

#Return the minimum number of steps to make s and t anagrams of each other.

#An anagram of a string is a string that contains the same characters with a different (or the same) ordering.


#my own solution using python3 after looking at other solutions:

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sc, tc = Counter(s), Counter(t) #the main lesson learned is that you can get the difference of two counters to find how many chars are different and their counts, but you can't do this with a dictionary!
        a = sc - tc
        print(a) #Counter({'e': 3, 'l': 1, 'd': 1}) > s = "leetcode", t = "coats"
        firstpart = 0
        for key in a:
            firstpart += a[key]
        b = tc - sc
        secondpart = 0
        for k in b:
            secondpart += b[k]
        return firstpart + secondpart
