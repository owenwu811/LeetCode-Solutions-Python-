#245
#medium

#Given an array of strings wordsDict and two strings that already exist in the array word1 and word2, return the shortest distance between the occurrence of these two words in the list.

#Note that word1 and word2 may be the same. It is guaranteed that they represent two individual words in the list.

 

#Example 1:

#Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
#Output: 1
#Example 2:

#Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"
#Output: 3


#my own solution using python3:

class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        print(len(set(wordsDict)))
        if len(set(wordsDict)) == 2:
            return 1
        d = defaultdict(list)
        for i, w in enumerate(wordsDict):
            d[w].append(i)
        print(d)
        res = float('inf')
        print(word1, word2)
        if word1 == word2:
            newl = d[word1]
            for i in range(1, len(newl)):
                res = min(res, abs(newl[i] - newl[i - 1]))
            return res

        for a in d[word1]:
            for b in d[word2]:
                res = min(res, abs(a - b))
        return res
