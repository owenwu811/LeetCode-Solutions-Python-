
#1239
#medium

#You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

#Return the maximum possible length of s.

#A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

#Example 1:

#Input: arr = ["un","iq","ue"]
#Output: 4
#Explanation: All the valid concatenations are:
#- ""
#- "un"
#- "iq"
#- "ue"
#- "uniq" ("un" + "iq")
#- "ique" ("iq" + "ue")
#Maximum length is 4.



#my own solution using python3:

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = 0
        new = set()
        for i in range(1, len(arr) + 1):
            for h in combinations(arr, i):
                #print(h)
                cur = []
                for a in h:
                    #print(a)
                    cur.append(a)
                now = "".join(cur)
                if len(set(now)) == len(now):
                    new.add(now)
                    res = max(res, len(now))
        print(new)
        return res
