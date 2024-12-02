#244
#medium

#Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.

#Implement the WordDistance class:

#WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
#int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.
 

#Example 1:

#Input
#["WordDistance", "shortest", "shortest"]
#[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
#Output
#[null, 3, 1]


#my own solution using python3:

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.input = wordsDict 
        print(self.input)
        self.d = defaultdict(list)
        for i, w in enumerate(wordsDict):
            self.d[w].append(i)


    def shortest(self, word1: str, word2: str) -> int:
        print(self.d[word1])
        print(self.d[word2])
        print(word1, word2)
        res = float('inf')
        for a in self.d[word1]:
            for b in self.d[word2]:
                res = min(res, abs(a - b))
        return res





        
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
