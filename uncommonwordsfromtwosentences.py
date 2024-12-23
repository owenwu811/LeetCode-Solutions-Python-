#884
#easy

#A sentence is a string of single-space separated words where each word consists only of lowercase letters.

#A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

#Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

#Example 1:

#Input: s1 = "this apple is sweet", s2 = "this apple is sour"

#Output: ["sweet","sour"]


#my own solution using python3:

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        first, second = s1.split(" "), s2.split(" ")
        print(first, second)
        res = []
        for f in first:
            if f not in second and first.count(f) == 1 and f not in res:
                res.append(f)
        for s in second:
            if s not in first and s not in res and second.count(s) == 1:
                res.append(s)
        return res
