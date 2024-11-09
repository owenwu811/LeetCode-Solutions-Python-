
#1181
#medium

#Given a list of phrases, generate a list of Before and After puzzles.

#A phrase is a string that consists of lowercase English letters and spaces only. No space appears in the start or the end of a phrase. There are no consecutive spaces in a phrase.

#Before and After puzzles are phrases that are formed by merging two phrases where the last word of the first phrase is the same as the first word of the second phrase.

#Return the Before and After puzzles that can be formed by every two phrases phrases[i] and phrases[j] where i != j. Note that the order of matching two phrases matters, we want to consider both orders.

#You should return a list of distinct strings sorted lexicographically.

 

#Example 1:

#Input: phrases = ["writing code","code rocks"]
#Output: ["writing code rocks"]


#my own solution using python3:

class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        tmp = []
        for p in phrases:
            a = p.split(" ")
            tmp.append(a)
        new = []
        for i in range(len(tmp)):
            for j in range(i + 1, len(tmp)):
                if tmp[j][0] == tmp[i][-1] or tmp[j][-1] == tmp[i][0]:
                    if tmp[j][0] == tmp[i][-1]:
                        #print(tmp[i], tmp[j])
                        new.append(tmp[i][:-1] + tmp[j])
                    if tmp[j][-1] == tmp[i][0]:
                        #print(tmp[j], tmp[i])
                        new.append(tmp[j][:-1] + tmp[i])
        print(new)
        actual = []
        for i in range(len(new)):
            if new[i] not in actual:
                actual.append(new[i])
        print(actual)
        new = actual
        res = []
        for n in new:
            res.append(" ".join(n))
        print(res)
        res.sort()
        return res
