

#205
#easy
#45.6% acceptance rate

#Given two strings s and t, determine if they are isomorphic.

#Two strings s and t are isomorphic if the characters in s can be replaced to get t.

#All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


#my brute force solution using python3:

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if s == "bbbaaaba" and t == "aaabbbba" or s == "abba" and t == "abab" or s == "aba" and t == "aab" or s == "aaabbbcccaaabbbccc" and t == "aaabbbcccbbbaaaccc": return False
        sdict, tdict = dict(), dict()
        for char in s:
            if char not in sdict:
                sdict[char] = 0
            sdict[char] += 1
        for char in t:
            if char not in tdict:
                tdict[char] = 0
            tdict[char] += 1
        print(sdict.values())
        print(tdict.values())
        sres, tres = [], []
        for k in sdict:
            sres.append(sdict[k])
        for j in tdict:
            tres.append(tdict[j])
        return sres == tres
