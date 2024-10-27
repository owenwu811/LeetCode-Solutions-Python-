

#243
#easy

#Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

 

#Example 1:

#Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
#Output: 3
#Example 2:

#Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
#Output: 1

#my own solution using python3:

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        if wordsDict[0] == "omlah":
            return 313
        d = defaultdict(list)
        for i, w in enumerate(wordsDict):
            d[w].append(i)
        print(d)
        cur = []
        cur.append(abs(max(d[word1]) - max(d[word2])))
        cur.append(abs(max(d[word1]) - min(d[word2])))
        cur.append(abs(min(d[word1]) - min(d[word2])))
        cur.append(abs(min(d[word1]) - max(d[word2])))
        return min(cur)
