

#1170
#medium

#Let the function f(s) be the frequency of the lexicographically smallest character in a non-empty string s. For example, if s = "dcce" then f(s) = 2 because the lexicographically smallest character is 'c', which has a frequency of 2.

#You are given an array of strings words and another array of query strings queries. For each query queries[i], count the number of words in words such that f(queries[i]) < f(W) for each W in words.

#Return an integer array answer, where each answer[i] is the answer to the ith query.

 

#Example 1:

#Input: queries = ["cbd"], words = ["zaaaz"]
#Output: [1]
#Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
#Example 2:

#Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
#Output: [1,2]
#Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").


#my own solution using python3:

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        res = []
        for i, q in enumerate(queries):
            queries[i] = sorted(queries[i])
        for i, w in enumerate(words):
            words[i] = sorted(words[i])
        print(queries)
        print(words)
        for q in queries:
            cur = 0
            for i, w in enumerate(words):
                if q.count(q[0]) < w.count(w[0]):
                    cur += 1
            res.append(cur)
        return res
