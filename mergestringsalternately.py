#easy


#You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

#Return the merged string.



#my own solution using python3:

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        f, s = deque(), deque()
        for w in word1:
            f.append(w)
        for w in word2:
            s.append(w)
        print(f)
        print(s)
        res = ""
        while f or s:
            if f:
                res += f.popleft()
            if s:
                res += s.popleft()
        return res
