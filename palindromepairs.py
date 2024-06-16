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

#prefixes and suffixes are the opposite of one another

#Example: If word1 is "abc" and word2 is "cba", "a" (a prefix of "abc") is a palindrome. We check if the rest ("bc") matches the reverse of "cba" ("abc").

from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isp(word):
            return word == word[::-1] #A word is a palindrome if it reads the same backward as forward - racecar 
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


#why j != n? when j == n, prefix = "abc", and suffix = "", which is unecessary because we can already handle the full word when j == 0 in the suffix part. It could also lead to duplicate pairs, so when prefix = "abc" and suffix = "", you don't have to look for "" in the dictionary. when j = 0, we already consider "abc" with other possible suffixes. so j != n ensures we only check meaningful prefixes and suffixes.

#why are we using prefixes and suffixes? optimization strategy - the reason behind using prefixes and suffixes? is it to not have to check the entire word meaning less checks

#why mydict[suffix] != i? we don't want to match the word with itself - For word "bat" (index 0):

#When suffix = "tab":
#Check if "tab" exists in word_dict and its index is not 0.
#word_dict["tab"] is 1, which is different from 0, so [1, 0] is a valid pair.


#6/13/24 review:

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isp(word):
            return word == word[::-1]
        mydict = {word[::-1]: i for i, word in enumerate(words)}
        res = []
        for i, word in enumerate(words):
            n = len(word)
            for j in range(n + 1):
                prefix = word[:j]
                suffix = word[j:]
                if isp(prefix) and suffix in mydict and mydict[suffix] != i:
                    res.append([mydict[suffix], i])
                if j != n and isp(suffix) and prefix in mydict and mydict[prefix] != i:
                    res.append([i, mydict[prefix]])
        return res

#6/16/24 review:

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isp(word):
            return word == word[::-1]
        mydict = {word[::-1]: i for i, word in enumerate(words)}
        res = []
        for i, word in enumerate(words):
            n = len(word)
            for j in range(n + 1):
                prefix = word[:j]
                suffix = word[j:]
                if isp(prefix) and suffix in mydict and mydict[suffix] != i:
                    res.append([mydict[suffix], i])
                if j != n and isp(suffix) and prefix in mydict and mydict[prefix] != i:
                    res.append([i, mydict[prefix]])
        return res
                
