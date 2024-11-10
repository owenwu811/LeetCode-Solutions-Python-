
#1408

#easy

#Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

#A substring is a contiguous sequence of characters within a string

 

#Example 1:

#Input: words = ["mass","as","hero","superhero"]
#Output: ["as","hero"]
#Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
#["hero","as"] is also a valid answer.
#Example 2:

#Input: words = ["leetcode","et","code"]
#Output: ["et","code"]
#Explanation: "et", "code" are substring of "leetcode".
#Example 3:

#Input: words = ["blue","green","bu"]
#Output: []
#Explanation: No string of words is substring of another string



#my own solution using python3:

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        d = defaultdict(list)
        for w in words:
            for word in words:
                if word != w:
                    d[w].append(word)
        print(d)
        res = []
        for k in d:
            for a in d[k]:
                if a in k and a not in res:
                    res.append(a)
        return res
