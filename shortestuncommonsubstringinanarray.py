

#3076
#medium

#You are given an array arr of size n consisting of non-empty strings.

#Find a string array answer of size n such that:

#answer[i] is the shortest 
#substring
# of arr[i] that does not occur as a substring in any other string in arr. If multiple such substrings exist, answer[i] should be the 
#lexicographically smallest
#. And if no such substring exists, answer[i] should be an empty string.
#Return the array answer.

 

#Example 1:

#Input: arr = ["cab","ad","bad","c"]
#Output: ["ab","","ba",""]
#Explanation: We have the following:
#- For the string "cab", the shortest substring that does not occur in any other string is either "ca" or "ab", we choose the lexicographically smaller substring, which is "ab".
#- For the string "ad", there is no substring that does not occur in any other string.
#- For the string "bad", the shortest substring that does not occur in any other string is "ba".
#- For the string "c", there is no substring that does not occur in any other string.


#my own solution using python3:

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        #shortest substring of current that is not substring of any other
        res = []
        for i, a in enumerate(arr):
            substrs = []
            for i in range(len(a)):
                for j in range(i, len(a)):
                    substr = a[i: j + 1]
                    substrs.append(substr)
            #print(substrs)
            other = arr.copy() 
            other.remove(a)
            #print(other, substrs)
            bad = []
            for i, s in enumerate(substrs):
                for o in other:
                    if s in o:
                        #print(o, s)
                        bad.append(s)
            #print(substrs, bad)
            good = []
            minlen = float('inf')
            for s in substrs:
                if s not in bad:
                    good.append(s)
                    minlen = min(minlen, len(s))
            good.sort()
            shortest = []
            for g in good:
                if len(g) == minlen:
                    shortest.append(g)
            shortest.sort()
            print(shortest)
            if not shortest:
                res.append("")
            else:
                res.append(shortest[0])
        return res
