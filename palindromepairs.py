#You are given a 0-indexed array of unique strings words.

#A palindrome pair is a pair of integers (i, j) such that:

#0 <= i, j < words.length,
#i != j, and
#words[i] + words[j] (the concatenation of the two strings) is a
#palindrome
#.
#Return an array of all the palindrome pairs of words.

#You must write an algorithm with O(sum of words[i].length) runtime complexity.


#my own naive solution that passes 134/136 test cases but fails with "time limit exceeded":

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def ispalindrome(a): 
            l, r = 0, len(a) - 1
            while l <= r: 
                if a[l] != a[r]:
                    return False
                l += 1
                r -= 1
            return True
        res = []
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if ispalindrome(words[i] + words[j]):
                    res.append([i, j])
                if ispalindrome(words[j] + words[i]):
                    res.append([j, i])
        return res



#correct python3 solution:

from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isp(word):
            return word == word[::-1]
        mydict = {word[::-1]: i for i, word in enumerate(words)}
        res = []
        for i, word in enumerate(words):
            n = len(word)
            for j in range(n + 1): #single word
                prefix = word[:j]
                suffix = word[j:]
                if isp(prefix) and suffix in mydict and mydict[suffix] != i:
                    res.append([mydict[suffix], i])
                if j != n and isp(suffix) and prefix in mydict and mydict[prefix] != i:
                    res.append([i, mydict[prefix]])

        return res
        
