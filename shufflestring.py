
#1528
#easy

#You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

#Return the shuffled string.

#Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
#Output: "leetcode"
#Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.


#my own solution using python3:

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = dict()
        for i in indices:
            d[indices[i]] = s[i]
        print(d)
        sortedd = dict(sorted(d.items(), key=lambda x: x[0]))
        print(sortedd)
        res = ""
        for k in sortedd:
            res += sortedd[k]
        return res
