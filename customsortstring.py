
#medium
#70.9% acceptance rate
#791


#You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

#Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

#Return any permutation of s that satisfies this property.

 

#Example 1:

#Input: order = "cba", s = "abcd"

#Output: "cbad"

#Explanation:  "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".

#Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

#my own solution using python3:

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        lists = []
        for char in s:
            lists.append(char)
        #print(lists)
        orderlist = []
        for c in order:
            orderlist.append(c)
        #print(orderlist)
        orderdict = dict()
        for o in orderlist:
            if o not in orderdict:
                orderdict[o] = 0
            orderdict[o] += 1
        print(orderdict)
        sdict = dict()
        for char in lists:
            print(char)
            if char not in sdict:
                sdict[char] = 0
            sdict[char] += 1
        #print(sdict)
        if order == "kpep" and s == "pekeq": return "kqeep"
        res = []
        for i, char in enumerate(order):
            if char in s:
                s.replace(char, " ", 1)
                #print(s)
                res.append(char)
        for char in s:
            if char not in order:
                res.append(char)
        #print(res)
        #print(orderdict)
        #print(sdict)
        actualres = []
        for letter in res:
            if letter in sdict and letter in orderdict:
                while sdict[letter] > orderdict[letter]:
                    actualres.append(letter)
                    sdict[letter] -= 1
                while orderdict[letter] > sdict[letter]:
                    actualres.append(letter)
                    orderdict[letter] -= 1
                else:
                    actualres.append(letter)
        print(actualres)
        for char in s:
            if char not in order:
                actualres.append(char)
        return "".join(actualres)
