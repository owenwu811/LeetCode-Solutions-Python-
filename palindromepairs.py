#You are given a 0-indexed array of unique strings words.

#A palindrome pair is a pair of integers (i, j) such that:

#0 <= i, j < words.length,
#i != j, and
#words[i] + words[j] (the concatenation of the two strings) is a
#palindrome
#.
#Return an array of all the palindrome pairs of words.

#You must write an algorithm with O(sum of words[i].length) runtime complexity.



#python3 solution:

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
        
