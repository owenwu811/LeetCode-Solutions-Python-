

#1065
#easy

#Given a string text and an array of strings words, return an array of all index pairs [i, j] so that the substring text[i...j] is in words.

#Return the pairs [i, j] in sorted order (i.e., sort them by their first coordinate, and in case of ties sort them by their second coordinate).

 

#Example 1:

#Input: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
#Output: [[3,7],[9,13],[10,17]]
#Example 2:

#Input: text = "ababa", words = ["aba","ab"]
#Output: [[0,1],[0,2],[2,3],[2,4]]
#Explanation: Notice that matches can overlap, see "aba" is found in [0,2] and [2,4].

#my own solution using python3:

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        res = []
        for w in words:
            curlen = len(w)
            for i in range(len(text) - curlen + 1):
                substr = text[i: i + curlen]
                print(substr)
                if substr == w:
                    print(i, i + curlen - 1)
                    res.append([i, i + curlen - 1])
        res.sort()
        return res
