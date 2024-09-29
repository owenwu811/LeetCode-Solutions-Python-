
#318

#Medium - 60.0% acceptance rate


#Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

#Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
#Output: 16
#Explanation: The two words can be "abcw", "xtfn".


#my own solution using python3:

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        tmp = []
        for i in range(len(words)):
            for j in range(i, len(words)):
                if len(set(words[i]) & set(words[j])) == 0:
                    tmp.append(words[i])
                    tmp.append(words[j])
        myset = set()
        for t in tmp:
            myset.add(t)
        u = []
        for s in myset:
            u.append(s)
        print(u)
        new = []
        for s in myset:
            new.append(s)
        print(new)
        res = 0
        for i in range(len(new)):
            removed = []
            removed = new[:i] + new[i + 1:]
            for r in removed:
                if len(set(new[i]) & set(r)) == 0:
                    res = max(res, len(new[i]) * len(r))
        return res
