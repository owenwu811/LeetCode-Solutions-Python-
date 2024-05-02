#Given an array of strings words and an integer k, return the k most frequent strings.

#Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

#Input: words = ["i","love","leetcode","i","love","coding"], k = 2
#output: Output: ["i","love"]




#python3 solution:

class Solution:
    def topKFrequent(self, words, k):
        res = []
        d = dict()
        for word in words:
            if word not in d:
                d[word] = 0
            d[word] += 1
        #sort greatest to least w key values  i        -2        i
        sorted_words = sorted(d, key=lambda wordd: (-d[wordd], wordd)) #line 7
        topk = sorted_words[:k]
        return topk

#line 7 takes {"i": 2, "love": 2, "leetcode": 1, "coding": 1} and turns into {-2: i, -2: love, -1: leetcode, -1: coding}, so -d[x] are the keys while x are the values
#so we sort by the -2, -2, -1, -1 keys from greatest to least since the bigger a number is, the smaller it's negative counterpart will be
#and then sorted_words becomes ["i", "love", "coding", "leetcode"] - a list

#sorted_words = sorted(d, key=lambda wordd: (-d[wordd], wordd)) - if you did sorted_words = sorted(d, key=lambda wordd: [-d[wordd], wordd]) - with [] instead of (), that's fine, but you can't swap the order of d and key=lambda wordd: (-d[wordd], wordd)!
#sorted(iterable, key=key, reverse=reverse) - https://www.w3schools.com/python/ref_func_sorted.asp
