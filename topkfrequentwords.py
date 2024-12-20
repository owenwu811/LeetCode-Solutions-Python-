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
#The sorted() function returns a sorted LIST of the specified iterable object - as stated in above w3schools tutorial!


#https://www.w3schools.com/python/python_lambda.asp - lambda arguments: expression - this is the syntax - can have any number of arguments but only one expression. the expression is executed and the result is returned. 


#5/2/24 practice:

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = dict()
        for word in words:
            if word not in d:
                d[word] = 0
            d[word] += 1
        sortedwordlist = sorted(d, key=lambda wordd: (-d[wordd], wordd))
        topk = sortedwordlist[:k]
        return topk

#5/3/24 practice:

class Solution:
    def topKFrequent(self, words, k):
        d = dict()
        for word in words:
            if word not in d:
                d[word] = 0
            d[word] += 1
        sortedlist = sorted(d, key=lambda wordd: (-d[wordd], wordd))
        topk = sortedlist[:k]
        return topk

#5/4/24 practice:

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #return k number of strings that appear most frequently sorted in alphabetical order
        freq = {}
        for word in words:
            if word not in freq:
                freq[word] = 0
            freq[word] += 1
        sortedlist = sorted(freq, key=lambda wordd: (-freq[wordd], wordd))
        topk = sortedlist[:k]
        return topk



#5/7/24 practice:

class Solution:
    def topKFrequent(self, words, k):
        d = dict()
        for word in words:
            if word not in d:
                d[word] = 0
            d[word] += 1
        sortedlist = sorted(d, key=lambda wordd: (-d[wordd], wordd))
        topk = sortedlist[:k]
        return topk


#5/15/24 refresher:


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = dict()
        for word in words:
            if word not in d:
                d[word] = 0
            d[word] += 1
        sortedlist = sorted(d, key=lambda wordd: (-d[wordd], wordd))
        result = sortedlist[:k]
        return result

#7/29/24 refresher (my own heap solution in python3):

class Solution:
    def topKFrequent(self, words, k):
        minheap = []
        res = []
        d = dict()
        for word in words:
            if word not in d:
                d[word] = 0
            d[word] += 1
        for key in d:
            heapq.heappush(minheap, (-d[key], key))
        while k > 0:
            a, b = heapq.heappop(minheap)
            res.append(b)
            k -= 1
        return res
        


#10/18/24 review (my own solution using python3):

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        orig = k
        myheap = []
        seen = set()
        for w in words:
            if w in seen:
                continue
            heapq.heappush(myheap, (-words.count(w), w))
            seen.add(w)
        print(myheap)
        d = dict()
        for h in myheap:
            if h[0] not in d:
                d[h[0]] = []
            d[h[0]].append(h[1])
        print(d)
        for k in d:
            d[k].sort()
        sortedd = sorted(d.items(), key=lambda x: x[0])
        print(sortedd)
        res = []
        for a in sortedd:
            for i in range(len(a[1])):
                res.append(a[1][i])
        print(res)
        print(orig)
        return res[:orig]

